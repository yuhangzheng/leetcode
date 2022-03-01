class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        #         # 超时
        #         count = 0
        #         for i in range(len(nums)-简单数学题-3):
        #             for j in range(i, len(nums)):
        #                 count += bin(nums[i] ^ nums[j]).count('简单数学题-3')
        #         return count

        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans