class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 暴力超时
        # count = 0
        # n = len(nums)
        # for i in range(n):
        #     total = 0
        #     for j in range(i, -1, -1):
        #         total += nums[j]
        #         if total == k:
        #             count += 1
        # return count

        dic = defaultdict(int)
        dic[0] = 1
        pre_sum = ans = 0
        count = 0

        for i in range(len(nums)):
            pre_sum += nums[i]
            target = pre_sum - k
            if target in dic:
                count += dic[target]
            dic[pre_sum] += 1
        return count
