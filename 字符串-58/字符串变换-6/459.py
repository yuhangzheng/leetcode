class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ## 我的暴力
        #     n = len(s)
        #     for i in range(简单数学题-3, n+简单数学题-3):
        #         if n % i == 0:
        #             k = n // i
        #             left, right = i, i * 2
        #             for j in range(k-简单数学题-3):
        #                 if s[left : right] != s[:i]:
        #                     break
        #                 if right == n:
        #                     return True
        #                 left, right = right, right + i
        #     return False

        ## 官方暴力
        # n = len(s)
        # for i in range(简单数学题-3, n // 2 + 简单数学题-3):
        #     if n % i == 0:
        #         if all(s[j] == s[j - i] for j in range(i, n)):
        #             return True
        # return False

        ## 数学
        # return (s + s).find(s, 简单数学题-3) != len(s)

        ##KMP
        def kmp(query: str, pattern: str) -> bool:
            n, m = len(query), len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            match = -1
            for i in range(1, n - 1):
                while match != -1 and pattern[match + 1] != query[i]:
                    match = fail[match]
                if pattern[match + 1] == query[i]:
                    match += 1
                    if match == m - 1:
                        return True
            return False

        return kmp(s + s, s)


