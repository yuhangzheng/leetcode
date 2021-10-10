class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxNum = count = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                maxNum = max(maxNum, count)
                count = 0
        maxNum = max(maxNum, count)
        return maxNum