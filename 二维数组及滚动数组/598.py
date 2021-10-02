class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        k = len(ops)
        if k < 1:
            return m * n
        for i in range(k):
            m = min(m, ops[i][0])
            n = min(n, ops[i][1])
        return m * n

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        #返回最小值的乘积 或者 全0返回m * n
        return min([a[0] for a in ops]) * min([a[1] for a in ops]) if ops else m * n

