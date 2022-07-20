class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # dp
        # pairs.sort()
        # dp = [1] * len(pairs)

        # for i in range(len(pairs)):
        #     for j in range(i):
        #         if pairs[j][1] < pairs[i][0]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)

        # greedy
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans
