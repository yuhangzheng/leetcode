class Solution:
    def checkValidString(self, s: str) -> bool:
        # # 贪心，比栈好用（栈需要存储左括号和star的下标）
        # minLeft = maxLeft = 0
        # for l in s:
        #     if l == "(":
        #         minLeft += 1
        #         maxLeft += 1
        #     elif l == "*":
        #         minLeft = max(minLeft-1, 0)
        #         maxLeft += 1
        #     else:
        #         minLeft = max(minLeft-1, 0)
        #         maxLeft -= 1
        #         if maxLeft < 0:
        #             return False
        # return minLeft == 0

        # 动规
        n = len(s)
        dp = [[False] * (n+1) for _ in range(n+1)]
        for i, l in enumerate(s):
            if l == '*':
                dp[i][i] = True
        for i in range(1, n):
            c1 = s[i-1]
            c2 = s[i]
            dp[i-1][i] = (c1 == '(' or c1 == '*') and (c2 == ')' or c2 == '*')
        for i in range(n-3, -1, -1):
            c1 = s[i]
            for j in range(i+2, n):
                c2 = s[j]
                if ((c1 == '(' or c1 == '*') and (c2 == ')' or c2 == '*')):
                    dp[i][j] = dp[i+1][j-1]
                if not dp[i][j]:
                    for k in range(i, j):
                        dp[i][j] = dp[i][k] and dp[k+1][j]
        return dp[0][n - 1]
