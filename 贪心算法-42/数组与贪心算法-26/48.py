class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 旋转90° = 主对角线翻转 + 左右翻转
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(i+1, c):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(r):
            for j in range(c//2):
                matrix[i][j], matrix[i][c-j-1] = matrix[i][c-j-1], matrix[i][j]