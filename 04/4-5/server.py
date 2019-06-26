import socket
import json


def verify(data):
    """验证客户端握手信息"""
    data = data[:-4].split('\r\n')
    method = data.pop(0)  # 取出请求方式和协议
    header = {}
    # 将列表转为字典
    for key, val in enumerate(data):
        try:
            name, value = val.split(':')
        except Exception as exc:
            name, host, port = val.split(':')
            value = '{}:{}'.format(host, port)
        header[name] = value

    # 不满足条件则False
    if any(['GET' not in method, 'HTTP/1.1' not in method,
            header.get('Connection') != 'Upgrade',
            header.get('Upgrade') != 'websocket',
            header.get('Sec-WebSocket-Version') != '13',
            not header.get('Sec-WebSocket-Key'),
            not header.get('Origin')]):
        return False
    return True


def set_response(status):
    """设置响应头"""
    head = {'Status Code': '101 Web Socket Protocol Handshake', 'Connection': 'Upgrade', 'Upgrade': 'websocket',
            'Sec-WebSocket-Accept': 'T5ar3gbl3rZJcRmEmBT8vxKjdDo='}
    if not status:
        head = {'Status Code': '403'}
    headers = ['{}:{}'.format(k, item) for k, item in head.items()]
    headers.append('\r\n')
    res = '\r\n'.join(headers)
    return res.encode('utf8')


def verify_sting(conn):
    """读取客户端发送的消息并进行简单验证"""
    methods = ['GET', 'POST']
    while True:
        message = conn.recv(1024)
        if message:
            break
    message = json.loads(message)
    method = message.get('method')
    content = message.get('content')
    if method in methods:
        return content
    shake_hands_status = False  # 设置握手成功的状态，默认False


def get_data(content):
    data = {'huawei': '{"title": "Huawei latest flagship mobile P30 Pro", "price": 3999, "RAM": "8G", "ROM": "256G", "pixel": "4000W"}',
            'iphone': 'iOS'}
    return data.get(content)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 使用Python底层接口创建socket
    s.bind(('localhost', 50007))  # 绑定地址和端口
    s.listen(1)  # 只允许同时1个客户端连接
    conn, addr = s.accept()  # 客户端对象和客户端地址
    shake_hands_status = False  # 设置握手成功的状态，默认False
    with conn:
        # 读取客户端发送的消息
        data = conn.recv(1024).decode('utf8')
        if not shake_hands_status:
            # 避免重复握手
            status = verify(data)  # 校验握手信息
            resp = set_response(status)  # 根据握手校验结果返回响应头
            conn.send(resp)
            shake_hands_status = True  # 握手成功后对应状态

        # 以下为客户端消息校验和数据推送
        content = verify_sting(conn)
        if content:
            # 如果客户端消息通过校验则从数据从库中取出对应数据并推送给客户端
            data = get_data(content)
            conn.send(data.encode('utf8'))