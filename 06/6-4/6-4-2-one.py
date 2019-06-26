from fontTools.ttLib import TTFont
font = TTFont('movie.woff')  # 打开当前目录的movie.woff文件
font.saveXML('movie.xml')  # 另存为movie.xml