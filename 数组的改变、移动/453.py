#暴力算法不考虑， 数学法， 寻找每个点与最小点之间步长
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        move = 0
        minVal = float('inf')
        for i in range(len(nums)):
            move += nums[i]
            minVal = min(minVal, nums[i])
        return move - minVal * len(nums)


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        move = 0
        minVal = float('inf')
        for i in range(len(nums)):
            minVal = min(minVal, nums[i])
        for i in range(len(nums)):
            move += nums[i] - minVal
        return move