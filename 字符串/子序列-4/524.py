class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ## 双指针
        # dictionary.sort(key = lambda x : (-len(x), x))
        # for t in dictionary:
        #     i = j =0
        #     while i < len(t) and j < len(s):
        #         if t[i] == s[j]:
        #             i += 1
        #         j += 1
        #     if i == len(t):
        #         return t
        # return ""

        ## 动态规划
        m = len(s)
        # 二维矩阵
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                if ord(s[i]) == j + 97:
                    f[i][j] = i
                else:
                    f[i][j] = f[i + 1][j]

        res = ""
        for t in dictionary:
            match = True
            j = 0
            for i in range(len(t)):
                if f[j][ord(t[i]) - 97] == m:
                    match = False
                    break
                j = f[j][ord(t[i]) - 97] + 1
            if match:
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t
        return res