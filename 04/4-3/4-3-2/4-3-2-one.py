import tornado.ioloop
import tornado.web
import hashlib
import os
from datetime import datetime
from time import time


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 返回页面的视图
        self.render("index.html")

class FetHandler(tornado.web.RequestHandler):
    # 定义返回内容
    content = """
    <p>参团的游客，应听从领队、导游人员的安全提醒，切莫擅自行动。
        自身的人身、财物安全要注意，购买人身意外险，贵重物品要随身携带，
        不要留在车内或者交由他人保管。参加漂流、摩天轮等高风险项目的时候，
        要认真听从工作人员的安排，切莫求刺激而发生意外。</p>
    <p >以下是本次参团出行需要遵守的规范要求：</p>
    <p>一、跟刺激相比，命更重要，没有命就什么都没了。</p>
    <p>二、旅行中会遇到很多你从未见过的植物和动物，不要轻易打扰它们，有可能有毒。</p>
    <p>三、身体感觉不适，尤其是发烧、乏力和呕吐等情况必须报告随队医护人员。</p>
    <p>四、出发前请跟家人沟通好，避免造成失联错觉。</p>
    <p>五、出发前请按照队长的要求准备好必备衣物和干粮，最重要的是水。</p>
    <p>六、旅行途中必须紧跟队伍，不许在无人知晓的情况下行动。</p>
    <p>七、如不慎走失，请先释放信号弹，半小时后无人联系再想办法报警。</p>
    <p>八、如果不同意以上几条，请在出发前告知队长。</p>
    <p>九、最重要的是：没有命，就什么都没了。</p>
    """
    @staticmethod
    def deltas(tp):
        # 将前端传递的时间戳与当前时间戳对比并返回差值秒数
        tamp = int(tp)
        now = round(time())
        delta = datetime.fromtimestamp(now) - datetime.fromtimestamp(tamp)
        return delta.total_seconds()

    @staticmethod
    def hex5(value):
        # 使用 md5 加密值并返回加密后的字符串
        manipulator = hashlib.md5()
        manipulator.update(value.encode('utf-8'))
        return manipulator.hexdigest()

    def comparison(self, actions, tim, randstr, sign):
        # 根据传递的参数计算md5值，并与客户端提交的md5值进行比对
        value = actions+tim+randstr
        hexs = self.hex5(value)
        if sign == hexs:
            return True
        return False

    def get(self):
        # 返回数据的视图
        params = self.request.arguments  # 获取请求正文
        actions = params.get('actions')[0].decode('utf-8')
        tim = params.get('tim')[0].decode('utf-8')
        randstr = params.get('randstr')[0].decode('utf-8')
        sign = params.get('sign')[0].decode('utf-8')
        seconds = self.deltas(tim)  # 取双端时间差值
        if self.comparison(actions, tim, randstr, sign) and seconds < 5:
            # 如果双端 MD5 值和时间戳差值都符合要求则返回正常内容
            self.write(self.content)
        else:
            self.set_status(403)


def make_app():
    # 路由和静态文件路径设置
    return tornado.web.Application(
        [(r"/", MainHandler), (r"/fet", FetHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'template'),
        static_path=os.path.join(os.path.dirname(__file__), 'static')
    )


if __name__ == "__main__":
    # 绑定端口并启动
    app = make_app()
    app.listen(8206)
    tornado.ioloop.IOLoop.current().start()