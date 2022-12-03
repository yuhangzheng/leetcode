class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        n = len(nums)
        if (tot - target) % 2 != 0 or (tot - target) < 0:
            return 0

        neg = (tot - target) // 2
        # dp = [[0 for i in range(neg+1)] for j in range(n+1)]
        # dp[0][0] = 1
        # for i in range(1, n+1):
        #     for j in range(neg+1):
        #         num = nums[i-1]
        #         if num > j:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i-1][j-num]
        # print(dp)
        # return dp[n][neg]

        # 滚动数组 需要注意，内层循环要倒序遍历到num就行
        dp = [0 for i in range(neg + 1)]
        dp[0] = 1
        for num in nums:
            for j in range(neg, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[neg]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dfs
        # def dfs(idx: int, cur_sum: int) -> None:
        #     nonlocal res
        #     if idx == n:
        #         if cur_sum == target:
        #             res += 1
        #         return

        #     dfs(idx + 1, cur_sum + nums[idx])
        #     dfs(idx + 1, cur_sum - nums[idx])

        # n = len(nums)
        # res = 0
        # dfs(0, 0)
        # return res

        # 回溯
        def backtrace(idx: int) -> None:
            nonlocal res
            nonlocal path_sum
            if idx == n:
                if path_sum == target:
                    res += 1
                return
            path_sum += nums[idx]
            backtrace(idx + 1)
            path_sum -= nums[idx]

            path_sum -= nums[idx]
            backtrace(idx + 1)
            path_sum += nums[idx]

        n = len(nums)
        res = 0
        path_sum = 0
        backtrace(0)
        return res
