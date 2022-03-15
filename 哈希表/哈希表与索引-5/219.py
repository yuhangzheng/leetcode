# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         di = dict()
#         for i, s in enumerate(nums):
#             if s in di:
#                 if i - di.get(s) <= k:
#                     return True
#                 else:
#                     di[s] = i
#             else:
#                 di[s] = i
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False