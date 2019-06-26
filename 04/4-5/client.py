import socket
import base64
import random
import time
from urllib.parse import urlparse
import json


def get_url_info(url):
    """解析url"""
    url = urlparse(url)
    host = url.netloc
    resource = url.path or '/'
    return host, resource


def get_key():
    """生成key"""
    bytes_key = bytes(random.getrandbits(8) for _ in range(16))
    res = base64.b64encode(bytes_key).decode()
    return res


def get_header(url):
    """生成握手所需的信息"""
    key = get_key()
    host, resource = get_url_info(url)
    head = {'Connection': 'Upgrade', 'Upgrade': 'websocket',
            'Sec-WebSocket-Version': 13, 'Sec-WebSocket-Key': key,
            'Origin': '{}'.format(host)}
    headers = ['{}:{}'.format(k, item) for k, item in head.items()]
    headers.insert(0, 'GET {} HTTP/1.1'.format(resource))
    headers.append('\r\n')
    header = '\r\n'.join(headers)
    return header.encode('utf8')


def shake_hands(client, url):
    """发起握手并校验握手结果"""
    header = get_header(url)
    client.send(header)  # 发送握手信息
    time.sleep(5)
    # 读取服务端返回的握手结果
    message = client.recv(1024).decode('utf8')
    print(message)
    if 'Status Code:101' in message:
        return True
    return False


def receive_forever(client):
    """读取服务端返回的握手结果"""
    while True:
        time.sleep(5)
        message = client.recv(1024).decode('utf8')
        if message:
            print(message)


def send_message(client, message):
    """向服务端发送消息"""
    if isinstance(message, str):
        message = message.encode('utf8')
    if isinstance(message, bytes):
        client.send(message)


if __name__ == '__main__':
    url = 'ws://localhost:50007'
    host, resource = get_url_info(url)
    # 创建socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 50007))
    shake_hands_status = shake_hands(client, url)
    message = json.dumps({'method': 'GET', 'content': 'huawei'})  # 消息
    send_message(client, message)
    receive_forever(client)
    client.close()