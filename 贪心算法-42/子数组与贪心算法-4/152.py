class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp + 滚动
        # 维护一个最大乘积和一个最小乘积
        maxPro = minPro = ans = nums[0]
        for i in range(1, len(nums)):
            mx = maxPro
            mn = minPro
            maxPro = max(mx * nums[i], mn * nums[i], nums[i])
            minPro = min(mn * nums[i], mx * nums[i], nums[i])
            ans = max(maxPro, ans)
        return ans