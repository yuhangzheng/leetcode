class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # if c == 0: return True
        # for a in range(1, int(math.sqrt(c) + 1)):
        #     b = c - a * a
        #     if int(math.sqrt(b)) ** 2 == b:
        #         return True
        # return False

        # # 双指针
        # a = 0
        # b = int(math.sqrt(c))
        # while a <= b:
        #     if a*a + b*b == c:
        #         return True
        #     elif a*a + b*b > c:
        #         b -= 1
        #     else:
        #         a += 1
        # return False

#         费马平方和定理告诉我们：

# 一个非负整数 cc 如果能够表示为两个整数的平方和，当且仅当 cc 的所有形如 4k + 34k+3 的质因子的幂均为偶数。
        if not c:
            return True
        # (a - b) ^ 2 + (a + b) ^ 2 = 2 * (a ^ 2 + b ^ 2) = 2 * c
        while c % 2 == 0:
            c //= 2
        # 费马平方和定理
        if c % 4 == 3:
            return False
        sqrt = int(math.sqrt(c))
        for i in range(3, sqrt + 1, 4):
            count = 0
            while c % i == 0:
                c //= i
                count += 1
            if count % 2 != 0:
                return False
        return True
