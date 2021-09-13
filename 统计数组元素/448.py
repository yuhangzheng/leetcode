class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = - nums[abs(num) - 1]
        miss = []
        for index, num in enumerate(nums):
            if num > 0:
                miss.append(index + 1)
        return miss