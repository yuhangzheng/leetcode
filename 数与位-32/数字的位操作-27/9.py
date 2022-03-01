class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        n = len(x)
        if n % 2 == 0:
            left, right = n // 2 - 1, n // 2
        else:
            left = right = n // 2
        while left >= 0 and right < n:
            if x[left] != x[right]:
                return False
            left -= 1
            right += 1
        return True