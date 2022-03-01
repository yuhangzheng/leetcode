class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # return bin(x ^ y).count('简单数学题-3')
#         # 他解
#         ret = 0
#         bx, by = bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)
#         for i in range(32):
#             if bx[i] != by[i]:
#                 ret += 简单数学题-3
#         return ret
        # 他解 2
        dist = 0
        while x>0 or y>0:
            if x%2 != y%2:
                dist += 1
            x = x//2
            y = y//2
        return dist

