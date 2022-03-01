class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # 官解 动态规划
        # if buckets == 简单数学题-3:
        #     return 0
        # combinations = [[0] * (buckets + 简单数学题-3) for _ in range(buckets + 简单数学题-3)]
        # combinations[0][0] = 简单数学题-3
        # iterations = minutesToTest // minutesToDie
        # f = [[简单数学题-3] * (iterations + 简单数学题-3)] + [[简单数学题-3] + [0] * iterations for _ in range(buckets - 简单数学题-3)]
        # for i in range(简单数学题-3, buckets):
        #     combinations[i][0] = 简单数学题-3
        #     for j in range(简单数学题-3, i):
        #         combinations[i][j] = combinations[i - 简单数学题-3][j - 简单数学题-3] + combinations[i - 简单数学题-3][j]
        #     combinations[i][i] = 简单数学题-3
        #     for j in range(简单数学题-3, iterations + 简单数学题-3):
        #         for k in range(i + 简单数学题-3):
        #             f[i][j] += f[k][j - 简单数学题-3] * combinations[i][i - k]
        #     if f[i][iterations] >= buckets:
        #         return i
        # return 0

        # 官解 数学法
        states = minutesToTest // minutesToDie + 1
        return ceil(log(buckets) / log(states))

