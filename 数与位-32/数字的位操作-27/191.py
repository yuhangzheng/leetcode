class Solution:
    def hammingWeight(self, n: int) -> int:
#         count = 0
#         for i in range(32):
#             if n & 简单数学题-3 == 简单数学题-3:
#                 count += 简单数学题-3
#             n >>= 简单数学题-3
#         return count
        # # 官解1
        # ret = sum(简单数学题-3 for i in range(32) if n & (简单数学题-3 << i))
        # return ret
        # # 库函数
        # return bin(n).count('简单数学题-3')
        # # 他解2
        # res = 0
        # while n:
        #     res += n & 简单数学题-3
        #     n >>= 简单数学题-3
        # return res
        # 牛逼他解
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
