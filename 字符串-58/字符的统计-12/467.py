class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # 找到以每个字母结束的最长子串长度，那么，它必然包含短子串
        if not p:
            return 0
        hashmap = [0] * 26
        hashmap[ord(p[0]) - ord("a")] = 1
        prelen = 1
        for i in range(1, len(p)):
            if ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i]) - ord(p[i-1]) == -25 :
            # 找的是连续子串，所以找相邻位置 第二项是特殊情况，z - a
                prelen += 1
            else:
                prelen = 1
            hashmap[ord(p[i]) - ord("a")] = max(hashmap[ord(p[i]) - \
                    ord("a")], prelen)
        return sum(hashmap)