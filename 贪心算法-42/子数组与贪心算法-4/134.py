class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        # 暴力
        # # 考虑从每一个点出发
        # for i in range(n):
        #     j = i
        #     remain = gas[i]
        #     # 当前剩余的油能否到达下一个点
        #     while (remain - cost[j]) >= 0:
        #         # 减去花费的加上新的点的补给
        #         remain = remain - cost[j] + gas[(j + 1) % n]
        #         j = (j + 1) % n
        #         # j 回到了 i
        #         if j == i :
        #             return i

        # # 任何点都不可以
        # return -1

        # 从0开始找出最低点，如果最低点都不可以，那么从其他点出发也都不可以
        spare = 0
        minSpare = 1e4
        minIndex = 0
        for i in range(n):
            spare += gas[i] - cost[i]
            if spare < minSpare:
                minSpare = spare
                minIndex = i
        # 如果总共都不够，肯定不行，如果够，则从最低点的下一个点出发一定够
        return -1 if spare < 0 else (minIndex + 1) % n


