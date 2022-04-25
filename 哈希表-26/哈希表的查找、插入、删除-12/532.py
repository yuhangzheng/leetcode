class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # if k == 0:
        #     return len(set([i for i in nums if nums.count(i)>=2]))
        # nums.sort()
        # nums = set(nums)
        # count = 0
        # for i in nums:
        #     if i + k in nums:
        #         count += 1
        # return count

        # if k < 0:
        #     return 0
        # if k == 0:
        #     return len(set([i for i in nums if nums.count(i)>=2]))
        # cl = [i+k for i in nums]
        # return len(set(cl)&set(nums))

        res = set()
        seen = set()
        for i, num in enumerate(nums):
            if num - k in seen:
                res.add((num - k, num))
            if num + k in seen:
                res.add((num, num + k))
            seen.add(num)
        return len(res)
