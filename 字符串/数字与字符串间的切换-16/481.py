class Solution:
    def magicalString(self, n: int) -> int:
        if n < 4:
            return 1
        ## 暴力
        s = "122"
        i = 2
        while(i < len(s) and len(s) < n):
            if i % 2 == 0:
                s += '1' * int(s[i])
                i += 1
            else:
                s += '2' * int(s[i])
                i +=1
        return s[:n].count('1')
