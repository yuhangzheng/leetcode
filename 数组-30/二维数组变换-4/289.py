class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])
        ## 相邻坐标
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        for i in range(r):
            for j in range(c):

                live_nei = 0
                ## 查看相邻细胞
                for nei in neighbors:
                    row = i + nei[0]
                    col = j + nei[1]

                    if (row < r and row >= 0) and (col < c and col >= 0) and abs(board[row][col]) == 1:
                        live_nei += 1

                ## 规则 1 3  -1 表示活->死
                if board[i][j] == 1 and (live_nei < 2 or live_nei > 3):
                    board[i][j] = -1

                ## 规则 4   2 表示死->活
                if board[i][j] == 0 and live_nei == 3:
                    board[i][j] = 2

        for i in range(r):
            for j in range(c):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0