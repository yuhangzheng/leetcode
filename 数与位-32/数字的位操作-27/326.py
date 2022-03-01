class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # while n and n % 3 == 0:
        #     n //= 3
        # return n == 简单数学题-3
        return n > 0 and 3 ** 19 % n == 0