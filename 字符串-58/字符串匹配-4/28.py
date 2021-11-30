class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        def compute_prefix(needle):
            pre, k = [-1] * m, -1
            for i in range(1, m):
                while k > -1 and needle[k + 1] != needle[i]:
                    k = pre[k]
                if needle[k + 1] == needle[i]:
                    k += 1
                pre[i] = k
            return pre

        pre, k = compute_prefix(needle), -1
        for i in range(n):
            while k > -1 and needle[k + 1] != haystack[i]:
                k = pre[k]
            if needle[k + 1] == haystack[i]:
                k += 1
            if k == m - 1:
                return i - (m - 1)
        return -1
