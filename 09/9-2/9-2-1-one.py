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