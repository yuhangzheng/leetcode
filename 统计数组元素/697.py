class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = dict()
        for i, num in enumerate(nums):
            if num in dic:
                dic[num][0] += 1
                dic[num][2] = i
            else:
                dic[num] = [1, i, i]

        maxNum = minLen = 0
        for count, left, right in dic.values():
            if maxNum < count:
                maxNum = count
                minLen = right - left + 1
            elif maxNum == count:
                minLen = min(minLen, right - left + 1)
        return minLen