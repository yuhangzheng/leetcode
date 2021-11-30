class Solution:
    def shortestPalindrome(self, s: str) -> str:
        ## 官解 投机取巧
        # n = len(s)
        # base, mod = 131, 10**9 + 7
        # left = right = 0
        # mul = 1
        # best = -1

        # for i in range(n):
        #     left = (left * base + ord(s[i])) % mod
        #     right = (right + mul * ord(s[i])) % mod
        #     if left == right:
        #         best = i
        #     mul = mul * base % mod

        # add = ("" if best == n - 1 else s[best+1:])
        # return add[::-1] + s

        ## KMP
        n = len(s)
        fail = [-1] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1

        best = -1
        for i in range(n - 1, -1, -1):
            while best != -1 and s[best + 1] != s[i]:
                best = fail[best]
            if s[best + 1] == s[i]:
                best += 1

        add = ("" if best == n - 1 else s[best + 1:])
        return add[::-1] + s
