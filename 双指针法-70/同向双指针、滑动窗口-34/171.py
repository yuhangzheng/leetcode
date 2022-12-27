class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        p, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while p + 1 < n and s[p + 1] not in occ:
                occ.add(s[p + 1])
                p += 1
            ans = max(ans, p - i + 1)
        return ans