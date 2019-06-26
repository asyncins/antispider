# 定义映射关系
mappings = {'vhk08k': 0, 'vhk6zl': 1, 'vhk9or': 2,
            'vhkfln': 3, 'vhkbvu': 4, 'vhk84t': 5,
            'vhkvxd': 6, 'vhkqsc': 7, 'vhkjj4': 8,
            'vhk0f1': 9}
# HTML中得到的属性值
html_d_class = 'vhkvxd'
# 将映射后的结果打印输出
print(mappings.get(html_d_class))