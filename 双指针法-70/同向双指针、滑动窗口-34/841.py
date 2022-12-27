class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        res = 0
        l = 0
        r = 1
        while r < n:
            if nums[r] > nums[r-1]:
                r += 1
            else:
                res = max(res, r-l)
                l = r
                r += 1
        return max(res, r-l)