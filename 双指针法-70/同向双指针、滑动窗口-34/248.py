class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        p = 2
        q = 2
        while q < n:
            if nums[p-2] != nums[q]:
                nums[p] = nums[q]
                p += 1
            q += 1
        return p
