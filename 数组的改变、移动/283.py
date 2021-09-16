class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = q = 0
        n = len(nums)
        while(q < n):
            if nums[q] !=0:
                nums[p],nums[q] = nums[q], nums[p]
                p += 1
            q += 1
