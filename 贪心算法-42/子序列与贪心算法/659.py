class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        countMap = collections.Counter(nums)    # 存储剩余数字
        endMap = collections.Counter()  # 存储以x结尾的序列数量

        for x in nums:
            if countMap[x] > 0:
                if (prevEndCount := endMap.get(x-1, 0)) > 0:
                    countMap[x] -= 1
                    endMap[x-1] = prevEndCount - 1
                    endMap[x] += 1
                else:
                    if countMap.get(x+1, 0) > 0 and countMap.get(x+2, 0) > 0:
                        endMap[x+2] += 1
                        countMap[x] -= 1
                        countMap[x+1] -= 1
                        countMap[x+2] -= 1
                    else:
                        return False
        return True


