import io
import requests
from urllib.parse import urljoin
from parsel import Selector
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

url = 'http://www.porters.vip/confusion/recruit.html'
resp = requests.get(url)
sel = Selector(resp.text)
# 从响应正文中提取图片名称
image_name = sel.css('.pn::attr("src")').extract_first()
# 拼接图片名和URL
image_url = urljoin(url, image_name)
# 请求图片，拿到图片的字节流内容
image_body = requests.get(image_url).content
# 使用Image.open打开图片字节流，得到图片对象
image_stream = Image.open(io.BytesIO(image_body))
# 使用光学字符识别从图片对象中读取文字并打印输出结果
print(pytesseract.image_to_string(image_stream))