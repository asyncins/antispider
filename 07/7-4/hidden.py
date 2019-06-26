import tornado.ioloop
import tornado.web
import os


blacks = set()


class MainHandler(tornado.web.RequestHandler):
    """首页"""
    def get(self):
        # 获取客户端ip
        client = self.request.remote_ip
        # 将该视图与模板文件夹中的details.html文件绑定
        self.render("details.html")
class DetailHandler(tornado.web.RequestHandler):
    """简单的详情页"""
    def get(self):
        # 获取客户端IP
        client = self.request.remote_ip
        if client not in blacks:
            # 如果客户端IP不在黑名单则返回数据
            params = self.request.arguments  # 获取请求正文
            phone = params.get('phone')[0].decode('utf-8')
            self.finish("%s's data,you get." % phone)
        else:
            # 将响应状态码设置为403并返回提示信息
            self.set_status(403)
            self.finish('Got a spider.')


class HunterHandler(tornado.web.RequestHandler):
    """访问到该接口的客户端IP都加入黑名单"""
    def get(self):
        # 获取客户端IP
        client = self.request.remote_ip
        if client not in blacks:
            blacks.add(client)
        # 将响应状态码设置为403并返回提示信息
        self.set_status(403)
        self.finish('Got a spider.')

def make_app():
    # 路由和静态文件路径设置
    return tornado.web.Application(
        [(r"/", MainHandler), (r"/detail/", DetailHandler), (r"/details/", HunterHandler)],
        template_path=os.path.join(os.path.dirname(__file__), 'template'),
        static_path=os.path.join(os.path.dirname(__file__), 'static')
    )


if __name__ == "__main__":
    # 绑定端口并启动
    app = make_app()
    app.listen(8202)
    tornado.ioloop.IOLoop.current().start()