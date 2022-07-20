class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = 0
        res = []
        while n < len(nums):
            if n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                start = n
                while n+1 < len(nums) and nums[n]+1 == nums[n+1]:
                    n += 1
                res.append("{}->{}".format(nums[start],nums[n]))
            else:
                res.append(str(nums[n]))
            n +=1
        return res