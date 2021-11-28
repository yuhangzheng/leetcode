class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        #strs = sorted(strs, key = len)[::-1]
        strs.sort(key = lambda x : -len(x))
        if strs.count(strs[0]) == 1:
            return len(strs[0])
        for i in range(len(strs)):
            if strs.count(strs[i]) == 1:
                for j in range(i):
                    m = n =0
                    while m < len(strs[i]) and n < len(strs[j]):
                        if strs[i][m] == strs[j][n]:
                            m += 1
                        n += 1
                    if m == len(strs[i]):
                        break
                    else:
                        return len(strs[i])
        return -1