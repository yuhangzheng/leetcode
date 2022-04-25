class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        voc = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 not in voc:
                if c2 in voc.values():
                    return False
                voc[c1] = c2
            else:
                if voc[c1] != c2:
                    return False
        return True