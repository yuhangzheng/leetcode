class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        flag = True
        if  num < 0:
            flag = False
            num = -num
        res  = []
        while num:
            res.append(str(num % 7))
            num = num // 7
        if flag == False:
            res.append('-')
        return ''.join(res[::-1])