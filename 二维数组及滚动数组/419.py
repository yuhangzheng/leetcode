class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row = len(board)
        col = len(board[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == '.': continue
                if i > 0 and board[i-1][j] == 'X': continue  #战舰中间
                if j > 0 and board[i][j-1] == 'X': continue  #战舰中间
                count += 1
        return count