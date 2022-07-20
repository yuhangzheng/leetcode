class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_array = [-10^4] * k
        min_k = k_array[0]
        for i in range(len(nums)):
            if nums[i] > min_k:
                k_array.remove(min_k)
                k_array.append(nums[i])
            min_k = min(k_array)
        return min_k

        # def quickSelect(nums, left, right, k):
        #     pivot = random.randint(left, right)
        #     nums[right], nums[pivot] = nums[pivot], nums[right]

        #     i = j = left
        #     while j < right:
        #         if nums[j] <= nums[right]:
        #             nums[i], nums[j] = nums[j], nums[i]
        #             i += 1
        #         j += 1
        #     nums[i], nums[j] = nums[j], nums[i]

        #     if i < right - k + 1:
        #         return quickSelect(nums, i + 1, right, k)
        #     elif i > right - k + 1:
        #         return quickSelect(nums, left, i - 1, k - (right - i + 1))
        #     else:
        #         return nums[i]
        # return quickSelect(nums, 0, len(nums) - 1, k)