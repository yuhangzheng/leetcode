class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 官解 动态规划
        # if buckets == 1:
        #     return 0
        # combinations = [[0] * (buckets + 1) for _ in range(buckets + 1)]
        # combinations[0][0] = 1
        # iterations = minutesToTest // minutesToDie
        # f = [[1] * (iterations + 1)] + [[1] + [0] * iterations for _ in range(buckets - 1)]
        # for i in range(1, buckets):
        #     combinations[i][0] = 1
        #     for j in range(1, i):
        #         combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j]
        #     combinations[i][i] = 1
        #     for j in range(1, iterations + 1):
        #         for k in range(i + 1):
        #             f[i][j] += f[k][j - 1] * combinations[i][i - k]
        #     if f[i][iterations] >= buckets:
        #         return i
        # return 0

        # 官解 数学法
        states = minutesToTest // minutesToDie + 1
        return ceil(log(buckets) / log(states))

