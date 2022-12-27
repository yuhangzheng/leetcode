class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        nums.sort()
        res = 0
        for l in range(n):
            r = l
            for m in range(l+1, n):
                while r + 1 < n and nums[r+1] < nums[l] + nums[m]:
                    r += 1
                res += max(r-m, 0)
        return res
