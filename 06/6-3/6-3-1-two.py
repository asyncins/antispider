# 定义映射关系
mappings = {'vhk08k': 0, 'vhk6zl': 1, 'vhk9or': 2,
            'vhkfln': 3, 'vhkbvu': 4, 'vhk84t': 5,
            'vhkvxd': 6, 'vhkqsc': 7, 'vhkjj4': 8,
            'vhk0f1': 9}
# 商家联系电话class属性
html_d_class = ['vhkbvu', 'vhk08k', 'vhk08k',
                '', 'vhk84t', 'vhk6zl',
                'vhkqsc', 'vhkqsc', 'vhk6zl']

phone = [mappings.get(i) for i in html_d_class]
# 将映射后的结果打印输出
print(phone)