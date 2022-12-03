class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 不需要连续，以下解答错误
        # i = 1
        # cnt = 1
        # while i < len(nums):
        #     if nums[i] > nums[i-1]:
        #         cnt += 1
        #         if cnt == 3:
        #             return True
        #     else:
        #         cnt = 1
        #     i += 1
        # return False

        # # 左右数组记录最大最小值
        # n = len(nums)
        # left = [0] * n
        # right = [0] * n
        # left[0] = nums[0]
        # right[n-1] = nums[n-1]
        # for i in range(1, n):
        #     left[i] = min(left[i-1], nums[i])
        # for i in range(n-2, -1, -1):
        #     right[i] = max(right[i+1], nums[i])
        # for i in range(n):
        #     if left[i] < nums[i] < right[i]:
        #         return True
        # return False

        # Ｏ(1)
        first = nums[0]
        second = float('inf')
        for i in range(1, len(nums)):
            print(nums[i])
            if nums[i] > second:
                return True
            if first < nums[i]:
                second = nums[i]
            if nums[i] < first:
                first = nums[i]
        return False
