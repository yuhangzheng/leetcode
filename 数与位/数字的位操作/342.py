class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ## n的二进制只能有一个1且后面必有偶数个0
        # return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1