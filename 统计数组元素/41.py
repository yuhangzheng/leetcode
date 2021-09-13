class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for index, num in enumerate(nums):
            if num <= 0:
                nums[index] = n + 1
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
