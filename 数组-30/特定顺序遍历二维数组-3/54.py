class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        res = list()
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while up <= down and left <= right:
            for i in range(left, right+1):
                res.append(matrix[up][i])
            for j in range(up+1, down+1):
                res.append(matrix[j][right])
            if up < down and left < right:
                for i in range(right-1, left, -1):
                    res.append(matrix[down][i])
                for j in range(down, up, -1):
                    res.append(matrix[j][left])
            up, down, left, right = up + 1, down - 1, left + 1, right - 1
        return res