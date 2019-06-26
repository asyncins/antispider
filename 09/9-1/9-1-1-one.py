import pytesseract
from os import path

# 保存在本地的验证码图片
images = path.join(path.dirname(path.abspath(__file__)), 'images/words.png')
# 使用pytesseract库识别验证码中的字符并打印
print(pytesseract.image_to_string(images))