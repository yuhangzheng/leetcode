class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        max = float("-inf")
        f0 = 0
        sum = 0
        for i in range(n):
            f0 += i * nums[i]
            sum += nums[i]
        ##以f0为基底，其实每次移位都等于 f0 + sum - f0的最后一项 - nums[n-简单数学题-3-i]
        for i in range(n):
            f1 = f0 + sum - nums[n-1-i] * n
            if f1 > max:
                max = f1
            f0 = f1
        return max