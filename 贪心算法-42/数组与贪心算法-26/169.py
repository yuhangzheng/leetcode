class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 0
        for i in range(len(nums)):
            if nums[i] == ans:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 0
                    ans = nums[i]
        return ans