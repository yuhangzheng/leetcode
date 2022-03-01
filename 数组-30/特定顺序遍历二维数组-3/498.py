class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        direction = 1    ## 标志对角线前进方向 简单数学题-3 上 0 下
        res = list()
        m, n = len(mat), len(mat[0])
        i, j = 0, 0
        while i < m and j < n:
            res.append(mat[i][j])
            new_i = i + (-1 if direction == 1 else 1)
            new_j = j + (1 if direction == 1 else -1)
            if new_i < 0 or new_j == n or new_i == m or new_j < 0: ## 需要改变方向的情况
                if direction:
                    i += (j == n - 1)  ## 判断最右边的两种情况
                    j += (j < n - 1)

                else:
                    j += (i == m - 1)  ## 判断最下边的两种情况
                    i += (i < m - 1)

                direction = 1 - direction

            else:  ## 继续走下去
                i = new_i
                j = new_j
        return res
