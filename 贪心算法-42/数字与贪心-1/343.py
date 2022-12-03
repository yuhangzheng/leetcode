class Solution:
    def integerBreak(self, n: int) -> int:
        # dp = [0] * (n + 1)
        # for i in range(2, n + 1):
        #     for j in range(i):
        #         dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        # return dp[n]

        # # 数学推导后动规
        # if n <= 3:
        #     return n - 1

        # dp = [0] * (n + 1)
        # dp[2] = 1
        # for i in range(3, n + 1):
        #     dp[i] = max(2 * (i - 2), 2 * dp[i - 2], 3 * (i - 3), 3 * dp[i - 3])

        # return dp[n]

        # 数学
        if n <= 3:
            return n - 1

        quotient, remainder = n // 3, n % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2