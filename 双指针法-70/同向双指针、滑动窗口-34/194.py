class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return n
        p = 0
        q = 0
        while q < n:
            if nums[q] == nums[p]:
                q += 1
                continue
            else:
                p += 1
                nums[p] = nums[q]
        return p + 1
