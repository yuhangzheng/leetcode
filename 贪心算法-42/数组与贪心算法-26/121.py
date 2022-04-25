class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        buy = prices[0]
        difference = 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                difference = max(difference, prices[i] - buy)
            else:
                buy = prices[i]
        return difference
