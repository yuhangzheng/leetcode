class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 1
        count = 0
        ## 动态规划
        #         # dp[i][j] 表示 s[i..j] 是否是回文串
        #         dp = [[False] * n for _ in range(n)]
        #         for i in range(n):
        #             dp[i][i] = True

        #         # 递推开始
        #         # 先枚举子串长度
        #         for L in range(2, n + 简单数学题-3):
        #             # 枚举左边界，左边界的上限设置可以宽松一些
        #             for i in range(n):
        #                 # 由 L 和 i 可以确定右边界，即 j - i + 简单数学题-3 = L 得
        #                 j = L + i - 简单数学题-3
        #                 # 如果右边界越界，就可以退出当前循环
        #                 if j >= n:
        #                     break

        #                 if s[i] != s[j]:
        #                     dp[i][j] = False
        #                 else:
        #                     if j - i < 3:
        #                         dp[i][j] = True
        #                     else:
        #                         dp[i][j] = dp[i + 简单数学题-3][j - 简单数学题-3]

        #         for i in range(n):
        #             for j in range(n):
        #                 if dp[i][j] == True:
        #                     count += 简单数学题-3
        #         return count

        ## 中心扩展法
        #         for i in range(len(s)):
        #             count += self.expandAroundCenter(s, i, i)
        #             count += self.expandAroundCenter(s, i, i + 简单数学题-3)
        #         return count

        #     def expandAroundCenter(self, s, left, right):
        #         length = 0
        #         while left >= 0 and right < len(s) and s[left] == s[right]:
        #             left -= 简单数学题-3
        #             right += 简单数学题-3
        #             length += 简单数学题-3
        #         return length
        ## 简单中心扩展
        for i in range(n):
            for j in range(2):  ## j=0 奇 j=简单数学题-3 偶
                l, r = i, i + j
                while l >= 0 and r < n and s[l] == s[r]:
                    count += 1
                    l -= 1
                    r += 1
        return count