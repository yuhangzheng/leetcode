class Solution:
    BIG = 2 ** 30
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and (n & (n - 1)) == 0
        # return n > 0 and (n & -n) == n
        # return n > 0 and Solution.BIG % n == 0

        # return n > 0 and (n & (n - 1)) == 0
        return n > 0 and (n & -n) == n