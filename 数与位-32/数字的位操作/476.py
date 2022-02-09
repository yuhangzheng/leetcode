class Solution:
    def findComplement(self, num: int) -> int:
        # str1 = bin(num)
        # res = 0
        # for i in range(3, len(str1)):
        #     if str1[i] == '0':
        #         res += 1
        #     res <<= 1
        # return res >> 1

        #         # 官解    找最高最1 构造mask
        #         highbit = 0
        #         for i in range(1, 30 + 1):
        #             if num >= (1 << i):
        #                 highbit = i
        #             else:
        #                 break

        #         mask = (1 << (highbit + 1)) - 1
        #         return num ^ mask
        # 他解    从最低位构造数字
        i = ans = 0
        while num:
            if not num & 1:
                ans += 1 << i
            num >>= 1
            i += 1
        return ans

