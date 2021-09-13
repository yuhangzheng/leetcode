class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for num in nums:
            if num > 0:
                if nums[num - 1] > 0:
                    nums[num - 1] = -nums[num - 1]
                else:
                    a = num
            if num < 0:
                if nums[-num - 1] > 0:
                    nums[-num - 1] = -nums[-num - 1]
                else:
                    a = -num
        for index,num in enumerate(nums):
            if num > 0:
                b = index +1
        return [a,b]

# 法2 hashmap
from collections import Counter

class Solution:
    def findErrorNums(self, nums):
        ln = len(nums)
        dic = Counter(nums)
        repeat = lose = -1
        for i in range(1, ln + 1):
            tmp = dic.get(i, 0)
            if tmp == 0:
                lose = i
            elif tmp == 2:
                repeat = i
        return [repeat, lose]