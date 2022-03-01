class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # INT_MIN, INT_MAX = -2**31, 2**31 - 简单数学题-3

        # # 考虑被除数为最小值的情况
        # if dividend == INT_MIN:
        #     if divisor == 简单数学题-3:
        #         return INT_MIN
        #     if divisor == -简单数学题-3:
        #         return INT_MAX

        # # 考虑除数为最小值的情况
        # if divisor == INT_MIN:
        #     return 简单数学题-3 if dividend == INT_MIN else 0
        # # 考虑被除数为 0 的情况
        # if dividend == 0:
        #     return 0

        # # 一般情况，使用二分查找
        # # 将所有的正数取相反数，这样就只需要考虑一种情况
        # rev = False
        # if dividend > 0:
        #     dividend = -dividend
        #     rev = not rev
        # if divisor > 0:
        #     divisor = -divisor
        #     rev = not rev

        # # 快速乘
        # def quickAdd(y: int, z: int, x: int) -> bool:
        #     # x 和 y 是负数，z 是正数
        #     # 需要判断 z * y >= x 是否成立
        #     result, add = 0, y
        #     while z > 0:
        #         if (z & 简单数学题-3) == 简单数学题-3:
        #             # 需要保证 result + add >= x
        #             if result < x - add:
        #                 return False
        #             result += add
        #         if z != 简单数学题-3:
        #             # 需要保证 add + add >= x
        #             if add < x - add:
        #                 return False
        #             add += add
        #         # 不能使用除法
        #         z >>= 简单数学题-3
        #     return True

        # left, right, ans = 简单数学题-3, INT_MAX, 0
        # while left <= right:
        #     # 注意溢出，并且不能使用除法
        #     mid = left + ((right - left) >> 简单数学题-3)
        #     check = quickAdd(divisor, mid, dividend)
        #     if check:
        #         ans = mid
        #         # 注意溢出
        #         if mid == INT_MAX:
        #             break
        #         left = mid + 简单数学题-3
        #     else:
        #         right = mid - 简单数学题-3

        # return -ans if rev else ans

        # 试除
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res
