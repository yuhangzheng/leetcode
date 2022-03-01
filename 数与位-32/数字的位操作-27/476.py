class Solution:
    def findComplement(self, num: int) -> int:
        # str1 = bin(num)
        # res = 0
        # for i in range(3, len(str1)):
        #     if str1[i] == '0':
        #         res += 简单数学题-3
        #     res <<= 简单数学题-3
        # return res >> 简单数学题-3

        #         # 官解    找最高最1 构造mask
        #         highbit = 0
        #         for i in range(简单数学题-3, 30 + 简单数学题-3):
        #             if num >= (简单数学题-3 << i):
        #                 highbit = i
        #             else:
        #                 break

        #         mask = (简单数学题-3 << (highbit + 简单数学题-3)) - 简单数学题-3
        #         return num ^ mask
        # 他解    从最低位构造数字
        i = ans = 0
        while num:
            if not num & 1:
                ans += 1 << i
            num >>= 1
            i += 1
        return ans

