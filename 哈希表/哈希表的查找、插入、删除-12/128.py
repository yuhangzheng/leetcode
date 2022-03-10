class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        # count = 1
        # tmp = 1
        # print(nums)
        # if not nums:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1] - 1:
        #         tmp += 1
        #     elif nums[i] == nums[i+1]:
        #         pass
        #     else:
        #         count = max(count, tmp)
        #         tmp = 1
        # return max(count, tmp)

        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak