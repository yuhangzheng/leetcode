# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         dic = {}
#         for i in range(len(nums)):
#             if nums[i] in dic:
#                 dic[nums[i]] += 1
#             else:
#                 dic[nums[i]] = 1
#         max_len = 0
#         for key in dic:
#             if key-1 in dic:
#                 if dic[key-1]+dic[key] > max_len:
#                     max_len = dic[key-1]+dic[key]
#             if key +1 in dic:
#                 if dic[key+1]+dic[key] > max_len:
#                     max_len = dic[key+1]+dic[key]
#         return max_len
# class Solution:
#     def findLHS(self, nums: List[int]) -> int:
#         cnt = Counter(nums)
#         return max((val + cnt[key + 1] for key, val in cnt.items() if key + 1 in cnt), default=0)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res, begin = 0, 0
        for end in range(len(nums)):
            while nums[end] - nums[begin] > 1:
                begin += 1
            if nums[end] - nums[begin] == 1:
                res = max(res, end - begin + 1)
        return res