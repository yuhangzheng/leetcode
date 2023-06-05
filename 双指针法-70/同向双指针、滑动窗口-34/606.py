class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)
        if n1 < n2:
            return []

        res = []
        count_s = [0] * 26
        count_p = [0] * 26

        for i in range(n2):
            count_s[ord(s[i]) - 97] += 1
            count_p[ord(p[i]) - 97] += 1

        if count_s == count_p:
            res.append(0)

        for i in range(n1 - n2):
            count_s[ord(s[i]) - 97] -= 1
            count_s[ord(s[i + n2]) - 97] += 1

            if count_s == count_p:
                res.append(i + 1)
        return res
