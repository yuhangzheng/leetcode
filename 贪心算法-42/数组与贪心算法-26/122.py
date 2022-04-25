class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(0, prices[i] - prices[i-1])
        return ans

        #dp
        # n = len(prices)
        # # dp[i][0] : 第i天结束时，手上没有股票的最大利润
        # # dp[i][1] : 第i天结束时，手上持有股票的最大利润
        # dp = [[0] * 2 for _ in range(n)]
        #
        # # 初始化
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        #
        # for i in range(1, n):
        #     # dp[i][0]：（前一天没有股票，前一天持有股票+当天卖出）的最大值
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     # dp[i][1]：（前一天持有股票，前一天没有股票+当天买入）的最大值
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        #
        # return dp[n - 1][0]

        # dp 滚动数组
        n = len(prices)

        dp0, dp1 = 0, -prices[0]  # 初始化
        for i in range(1, n):
            dp0, dp1 = max(dp0, dp1 + prices[i]), max(dp1, dp0 - prices[i])

        return dp0
