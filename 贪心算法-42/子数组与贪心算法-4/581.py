class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        #         copy = []
        #         for num in nums:
        #             copy.append(num)
        #         copy.sort()
        #         if copy == nums:
        #             return 0
        #         left = right = 0
        #         for i, num in enumerate(copy):
        #             if num == nums[i]:
        #                 continue
        #             else:
        #                 left = i
        #                 break

        #         for i in range(len(copy)-1, -1, -1):
        #             if copy[i] == nums[i]:
        #                 continue
        #             else:
        #                 right = i
        #                 break
        #         return right - left + 1

        # 一次遍历，左边界只会出现在一次反序的地方，同理右边界只会出现在逆序遍历第一次反序的地方
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1
        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]

        return 0 if right == -1 else right - left + 1