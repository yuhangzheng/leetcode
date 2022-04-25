class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # nums.sort()
        # res = 0
        # for i in range(len(nums)):
        #     if i % 2 != 1:
        #         res += nums[i]
        # return res

        # 官解
        nums.sort()
        return sum(nums[::2])
