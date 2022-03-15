class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = dict()
        for i in range(len(nums)):
            if target - nums[i] in di:
                return [i, di.get(target - nums[i])]
            elif nums[i] not in di:
                di[nums[i]] = i
        return [0,1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

