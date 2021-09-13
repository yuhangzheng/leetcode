class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            nums[num % n - 1] = nums[num % n - 1] + n
        res = []
        for index, num in enumerate(nums):
            if num /n > 2:
                res.append(index + 1)
        return res
