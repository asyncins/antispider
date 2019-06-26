class Custom64:
    comparison = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E',
                  '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J',
                  '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O',
                  '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T',
                  '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y',
                  '25': 'Z', '26': 'a', '27': 'b', '28': 'c', '29': 'd',
                  '30': 'e', '31': 'f', '32': 'g', '33': 'h', '34': 'i',
                  '35': 'j', '36': 'k', '37': 'l', '38': 'm', '39': 'n',
                  '40': 'o', '41': 'p', '42': 'q', '43': 'r', '44': 's',
                  '45': 't', '46': 'u', '47': 'v', '48': 'w', '49': 'x',
                  '50': 'y', '51': 'z', '52': '0', '53': '1', '54': '2',
                  '55': '3', '56': '4', '57': '5', '58': '6', '59': '7',
                  '60': '8', '61': '9', '62': '+', '63': '/', '65': '=',
                  }

    def encode(self, value: str, threshold: int = 4) -> str:
        # 对传入的字符进行编码，并返回编码结果
        value = ''.join(['0' + bin(ord(t))[2:] for t in value])
        inputs = self.shift(value, threshold)
        result = ''
        for i in inputs:
            if i == '0' * threshold:
                # 全为0则视为补位
                encoding = 65
            else:
                encoding = 0
                for key, v in enumerate(i):
                    # 二进制数按权相加得到十进制数
                    val = int(v) * pow(2, len(i) - 1 - key)
                    encoding += val
            # 从对照表中取值
            after = self.comparison.get(str(encoding))
            result += after
        return result

    def decode(self, value: str, threshold: int, group: int = 8) -> str:
        """对传入的字符串解码，得到原字符"""
        result = []
        coder = self.str2binary(value, threshold=threshold)
        bins = self.shift(''.join(coder), group)
        for i in range(len(bins)):
            binary = ''.join(bins)[i * group: (i + 1) * group]
            if binary != '0' * group:
                # 如果全为0则视为补位，无需处理
                result.append(''.join([chr(i) for i in [int(b, 2) for b in binary.split(' ')]]))
        return ''.join(result)

    def str2binary(self, value: str, threshold: int = 6) -> list:
        """字符串转十进制再转二进制"""
        result = []
        values = self.str2decimal(value)
        for i in values:
            # 判断是否为补位
            if i == '65':
                val = '0' * threshold
            else:
                val = '{:0{threshold}b}'.format(int(i), threshold=threshold)
            result.append(val)
        return result

    @staticmethod
    def shift(value: str, threshold: int, group: int = 24) -> list:
        """位数转换"""
        remainder = len(value) % group
        if remainder:
            # 如果有余数，则说明需要用0补位
            padding = '0' * (group - remainder)
            value += padding
        # 按照threshold值切割字符
        result = [value[i:i + threshold] for i in range(0, len(value), threshold)]
        return result

    def str2decimal(self, value: str) -> list:
        """使用Base64编码表做对照，取出字符串对应的十进制数"""
        keys = []
        for t in value:
            for k, v in self.comparison.items():
                if v == t:
                    keys.append(k)
        return keys


if __name__ == '__main__':
    # threshold 的值建议为 4/5/6
    cus = Custom64()
    encode_res = cus.encode('async', threshold=5)
    decode_res = cus.decode(encode_res, threshold=5)
    print(encode_res)
    print(decode_res)