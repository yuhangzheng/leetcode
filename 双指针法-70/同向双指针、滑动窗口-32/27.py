class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        for i,item in enumerate(nums):
            if item != val:
                nums[start] = item
                start += 1
        return start