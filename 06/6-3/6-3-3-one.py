url_css = 'http://www.porters.vip/confusion/css/food.css'
url_svg = 'http://www.porters.vip/confusion/font/food.svg'
css_class_name = 'vhkbvu'

import requests
css_resp = requests.get(url_css).text
svg_resp = requests.get(url_svg).text

import re
pile = '.%s{background:-(\d+)px-(\d+)px;}' % css_class_name
pattern = re.compile(pile)
css = css_resp.replace('\n', '').replace(' ', '')
coord = pattern.findall(css)
if coord:
    x, y = coord[0]
    x, y = int(x), int(y)

from parsel import Selector
svg_data = Selector(svg_resp)
texts = svg_data.xpath('//text')

axis_y = [i.attrib.get('y') for i in texts if y <= int(i.attrib.get('y'))][0]

svg_text = svg_data.xpath('//text[@y="%s"]/text()' % axis_y).extract_first()

font_size = re.search('font-size:(\d+)px', svg_resp).group(1)

position = x // int(font_size)

number = svg_text[position]
print(number)