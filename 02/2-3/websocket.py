import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket

async def startup(uri):
    async with AioWebSocket(uri) as aws:
        # 初始化 aiowebsocket 库的连接类
        converse = aws.manipulator
        # 设定需要向服务器发送的信息
        message = b'AioWebSocket - Async WebSocket Client'
        while True:
            # 不断的向服务器发送信息，并打印输出信息发送内容和时间
            await converse.send(message)
            print('{time}-Client send: {message}'
                  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message=message))
            # 不断的读取服务器推送给客户端的信息，并打印输出信息内容和时间
            mes = await converse.receive()
            print('{time}-Client receive: {rec}'
                  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))


if __name__ == '__main__':
    # 设定远程服务器地址
    remote = 'wss://echo.websocket.org'
    try:
        # 开启事件循环，调用并指定的方法
        asyncio.get_event_loop().run_until_complete(startup(remote))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')