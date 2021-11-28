class Solution:
    def countBinarySubstrings(self, s: str) -> int:
    #关键怎么得出不同组取min 等于 连续子串出现的个数。
        n = len(s)
        count = last = ans = p = 0
        while p < n:
            c = s[p]
            count = 0
            while(p < n and s[p] == c):
                p += 1
                count += 1
            ans += min(count,last)
            last = count
        return ans
