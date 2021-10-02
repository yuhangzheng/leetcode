class Solution:   #不对
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        if m <= 1 or n <= 1:
            return [[0]]
        ret = img.copy()
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0):  # 左上角
                    ret[i][j] = (ret[i + 1][j] + ret[i][j + 1] + ret[i + 1][j + 1]) // 4

                elif (i == 0 and j == n - 1):  # 右上角
                    ret[i][j] = (ret[i + 1][j] + ret[i][j - 1] + ret[i + 1][j - 1]) // 4

                elif (i == m - 1 and j == n - 1):  # 右下角
                    ret[i][j] = (ret[i - 1][j] + ret[i][j - 1] + ret[i - 1][j - 1]) // 4

                elif (i == m - 1 and j == 0):  # 左下角
                    ret[i][j] = (ret[i - 1][j] + ret[i][j + 1] + ret[i - 1][j + 1]) // 4

                elif (i != 0 and i != m - 1) and j == 0:  # 左边
                    ret[i][j] = (ret[i - 1][j] + ret[i + 1][j] + ret[i - 1][j + 1]
                                 + ret[i][j + 1] + ret[i + 1][j + 1]) // 6

                elif (i != 0 and i != m - 1) and j == n - 1:  # 右边
                    ret[i][j] = (ret[i - 1][j] + ret[i + 1][j] + ret[i - 1][j - 1]
                                 + ret[i][j - 1] + ret[i + 1][j - 1]) // 6

                elif (j != 0 and j != n - 1) and i == 0:  # 上边
                    ret[i][j] = (ret[i][j - 1] + ret[i][j + 1] + ret[i + 1][j + 1]
                                 + ret[i + 1][j - 1] + ret[i + 1][j]) // 6

                elif (j != 0 and j != n - 1) and i == m - 1:  # 下边
                    ret[i][j] = (ret[i][j - 1] + ret[i][j + 1] + ret[i - 1][j + 1]
                                 + ret[i - 1][j - 1] + ret[i - 1][j]) // 6

                elif (i != 0 and i != m - 1 and j != 0 and j != n - 1):  # 中间
                    ret[i][j] = (ret[i - 1][j - 1] + ret[i - 1][j] + ret[i - 1][j + 1]
                                 + ret[i][j - 1] + ret[i][j + 1] + ret[i + 1][j - 1]
                                 + ret[i + 1][j] + ret[i + 1][j + 1]) // 9
        return ret

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R, C = len(img), len(img[0])
        ans = [[0] * C for _ in img]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r-1, r, r+1):
                    for nc in (c-1, c, c+1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += img[nr][nc]
                            count += 1
                ans[r][c] = ans[r][c] // count

        return ans
