class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # return '{0:b}'.format(int(a, 2) + int(b, 2))
        # 传统
        flag = 0
        res = []
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len(a), len(b))):
            if i >= len(a):
                num1 = 0
            else:
                num1 = a[i]
            if i >= len(b):
                num2 = 0
            else:
                num2 = b[i]
            temp = int(num1) + int(num2) + flag

            if temp >= 2:
                temp -= 2
                flag = 1
            else:
                flag = 0
            res.append(temp)
        if flag == 1:
            res.append(1)
        res = [str(i) for i in res]
        return ''.join(res[::-1])