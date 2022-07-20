class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # n=len(nums)
        # nums=list(map(str,nums))
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]<nums[j]+nums[i]:
        #             nums[i],nums[j]=nums[j],nums[i]

        # return str(int("".join(nums)))

        # nums = list(map(str, nums))
        # def quickSort(nums):
        #     if len(nums) < 2:
        #         return nums
        #     elif len(nums) == 2:
        #         if nums[0] + nums[1] < nums[1] + nums[0]:
        #             nums[0], nums[1] = nums[1], nums[0]
        #         return nums
        #     else:
        #         pivot = nums[len(nums)//2]
        #         left , right = [], []
        #         nums.remove(pivot)
        #         for num in nums:
        #             if num + pivot >= pivot + num:
        #                 left.append(num)
        #             elif num + pivot < pivot + num:
        #                 right.append(num)
        #         return quickSort(left) + [pivot] + quickSort(right)
        # nums = quickSort(nums)
        # return str(int("".join(nums)))

        # nums = list(map(str, nums))
        # def partition(arr, low, high):
        #     i = low
        #     for j in range(low, high):
        #         if nums[j] + nums[high] >= nums[high] + nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #     nums[i], nums[high] = nums[high], nums[i]
        #     return i

        # def quickSort(nums, low, high):
        #     if low >= high:
        #         return
        #     else:
        #         if len(nums) < 2:
        #             return nums
        #         elif len(nums) == 2:
        #             if nums[0] + nums[1] < nums[1] + nums[0]:
        #                 nums[0], nums[1] = nums[1], nums[0]
        #             return nums
        #         else:
        #             pi = partition(nums, low, high)
        #             quickSort(nums, low, pi-1)
        #             quickSort(nums, pi+1, high)
        # quickSort(nums, 0, len(nums)-1)

        # return str(int("".join(nums)))

        def cmp(x, y):
            return 1 if x + y < y + x else -1

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))
        res = str(int("".join(nums)))
        return res