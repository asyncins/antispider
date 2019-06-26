try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from os import path


def handler(grays, threshold=160):
    """对灰度图片进行二值化处理
    默认阈值为160，可根据实际情况调整
    """
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    anti = grays.point(table, '1')
    return anti


# 保存在本地的验证码图片路径
images = path.join(path.dirname(path.abspath(__file__)), 'images/words.png')
# 图片灰度处理
gray = Image.open(images).convert('L')
# 图片二值化处理
image = handler(gray)
image.show()
# 使用pytesseract库识别验证码中的字符并打印
print(pytesseract.image_to_string(image))