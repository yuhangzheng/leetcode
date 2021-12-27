class Solution:
    def hammingWeight(self, n: int) -> int:
#         count = 0
#         for i in range(32):
#             if n & 1 == 1:
#                 count += 1
#             n >>= 1
#         return count
        # # 官解1
        # ret = sum(1 for i in range(32) if n & (1 << i))
        # return ret
        # # 库函数
        # return bin(n).count('1')
        # # 他解2
        # res = 0
        # while n:
        #     res += n & 1
        #     n >>= 1
        # return res
        # 牛逼他解
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
