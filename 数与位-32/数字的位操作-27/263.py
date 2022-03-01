class Solution:
    def isUgly(self, n: int) -> bool:
        #     if n == 0:
        #         return False
        #     flag = True
        #     while flag:
        #         if n % 5 == 0:
        #             n = n // 5
        #         elif n % 3 == 0:
        #             n = n // 3
        #         elif n % 2 == 0:
        #             n = n // 2
        #         else:
        #             flag = False
        #     return True if n == 简单数学题-3 else False
        if n <= 0:
            return False

        factors = [2, 3, 5]
        for factor in factors:
            while n % factor == 0:
                n //= factor

        return n == 1
