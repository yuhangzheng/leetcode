class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        tot = sum(machines)
        n = len(machines)
        if tot % n:
            return -1
        avg = tot // n
        ans, s = 0, 0
        # 注意题意，一次可以从几台洗衣机同时向一个方向传递一件衣服
        # s作为组间操作所需要的数量，num是自己本身所需要操作的数量
        for num in machines:
            num -= avg
            s += num
            ans = max(ans, abs(s), num)
        return ans
