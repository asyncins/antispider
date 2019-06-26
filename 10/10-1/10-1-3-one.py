from base64 import b64decode

code = ['d3d3Lmh1YXdlaS5jb20=', 'd3d3Lmp1ZWppbi5pbQ==']
for c in code:
    string = b64decode(c).decode('utf8')
    print(string)