try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from os import path


# 保存在本地的验证码图片路径
images = path.join(path.dirname(path.abspath(__file__)), 'images/mathes.png')
# 使用pytesseract库识别图中计算题并打印
print(pytesseract.image_to_string(images))
import re
# 将识别结果复制给 strings
strings = pytesseract.image_to_string(images)
# 从识别结果中提取数字
string = re.findall('\d+', strings)
# 从识别结果中提取运算符
operator = re.findall('[+|\-|\*]', strings)

def operator_func(a: int, b: int, oper: str) -> int:
    # 接收两个值和运算符，返回数学运算结果
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '*':
        return a * b

# 将识别结果传入运算方法，获得运算结果
res = operator_func(int(string[0]), int(string[1]), operator[0])
print(res)