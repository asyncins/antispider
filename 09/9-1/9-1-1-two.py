try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from os import path

# 保存在本地的验证码图片路径
images = path.join(path.dirname(path.abspath(__file__)), 'images/words.png')
# 图片灰度处理
gray = Image.open(images).convert('L')
# 显示处理后的图片
gray.show()