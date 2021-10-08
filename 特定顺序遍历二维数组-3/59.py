class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        up, down, left, right = 0, n - 1, 0, n - 1
        num = 1
        while up <= down and left <= right:
            for i in range(left, right+1):
                res[up][i] = num
                num += 1
            for j in range(up+1, down+1):
                res[j][right] = num
                num += 1
            if up < down and left < right:
                for i in range(right-1, left, -1):
                    res[down][i] = num
                    num += 1
                for j in range(down, up, -1):
                    res[j][left] = num
                    num += 1
            up, down, left, right = up + 1, down - 1, left + 1, right - 1
        return res