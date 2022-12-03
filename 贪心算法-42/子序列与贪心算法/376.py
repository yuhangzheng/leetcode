class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        #         # 上升摆动子序列
        #         up = [1] + [0] * (n-1)
        #         # 下降摆动子序列
        #         down = [1] + [0] * (n-1)

        #         for i in range(1, n):
        #             # 上升 down可以摆动 up不能摆了
        #             if nums[i] > nums[i-1]:
        #                 up[i] = max(up[i-1], down[i-1]+1)
        #                 down[i] = down[i-1]
        #             elif nums[i] < nums[i-1]:
        #                 up[i] = up[i-1]
        #                 down[i] = max(down[i-1], up[i-1]+1)
        #             else:
        #                 down[i] = down[i-1]
        #                 up[i] = up[i-1]
        #         return max(up[n-1],down[n-1])
        # up = down = 1
        # for i in range(1, n):
        #     if nums[i] > nums[i-1]:
        #         up = down + 1
        #     elif nums[i] < nums[i-1]:
        #         down = up + 1
        # return max(up, down)

        # 贪心

        result = 1
        preDiff = curDiff = 0
        for i in range(1, n):
            curDiff = nums[i] - nums[i - 1]
            if (curDiff < 0 and preDiff >= 0) or (curDiff > 0 and preDiff <= 0):
                result += 1
                preDiff = curDiff
        return result    