class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        #         # 超时
        #         count = 0
        #         for i in range(len(nums)-1):
        #             for j in range(i, len(nums)):
        #                 count += bin(nums[i] ^ nums[j]).count('1')
        #         return count

        n = len(nums)
        ans = 0
        for i in range(30):
            c = sum(((val >> i) & 1) for val in nums)
            ans += c * (n - c)
        return ans