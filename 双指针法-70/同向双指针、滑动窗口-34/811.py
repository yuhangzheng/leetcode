class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 超时
        # n = len(nums)
        # if n < k:
        #     return 0
        # res = -10**4
        # for i in range(0, n-k+1):
        #     s = 0
        #     for j in range(k):
        #         s += nums[i+j]/k
        #     res = max(res, s)
        # return res
        maxTotal = total = sum(nums[:k])
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)

        return maxTotal / k