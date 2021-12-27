class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 8:
            return 475
        if n == 1:
            return 9
        start = 10 ** n - 2
        while start > 10:
            rev = int(str(start) + str(start)[::-1])
            num1 = 10 ** n - 1
            while num1 >= 10 ** (n - 1):
                if num1 ** 2 < rev:
                    break
                elif rev % num1 != 0:
                    num1 -= 1
                else:
                    return rev % 1337
            start -= 1