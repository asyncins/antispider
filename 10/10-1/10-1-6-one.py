from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64


message = 'async'  # 消息原文

# 初始化乘积n长度为1024的RSA对象
rsa = RSA.generate(1024, Random.new().read)
# 生成私钥
private_key = rsa.exportKey()
# 生成公钥
public_key = rsa.publickey().exportKey()
# 打印私钥和公钥
print(private_key.decode('utf8'))
print(public_key.decode('utf8'))

# 将私钥和公钥存入对应名称的文件
with open('private.pem', 'wb') as f:
    f.write(private_key)

with open('public.pem', 'wb') as f:
    f.write(public_key)

with open('public.pem', 'r') as f:
    # 从文件中加载公钥
    pub = f.read()
    pubkey = RSA.importKey(pub)
    # 用公钥加密消息原文
    cipher = PKCS1_v1_5.new(pubkey)
    c = base64.b64encode(cipher.encrypt(message.encode('utf8'))).decode('utf8')

with open('private.pem', 'r') as f:
    # 从文件中加载私钥
    pri = f.read()
    prikey = RSA.importKey(pri)
    # 用私钥解密消息密文
    cipher = PKCS1_v1_5.new(prikey)
    m = cipher.decrypt(base64.b64decode(c), 'error').decode('utf8')

print('消息原文：%s\n消息密文:%s\n解密结果：%s' % (message, c, m))