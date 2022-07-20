class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # # 单指针
        # p = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         nums[i], nums[p] = nums[p], nums[i]
        #         p += 1
        # for i in range(p, n):
        #     if nums[i] == 1:
        #         nums[i], nums[p] = nums[p], nums[i]
        #         p += 1

        # 双指针
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1
