class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #         ##常规
        #         n, m = len(s), len(t)
        #         i = j = 0
        #         while i < n and j < m:
        #             if s[i] == t[j]:
        #                 i += 1
        #             j += 1
        #         return i == n

        ## 动态规划 进阶 -> 节省时间
        # dp 是二位矩阵
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        if dp[-1][-1] == len(s):
            return True
        return False