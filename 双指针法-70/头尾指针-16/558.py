class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c: str) -> bool:
            return c in "aeiouAEIOU"

        n = len(s)
        p, q = 0, n - 1
        s = list(s)
        while p < q:
            while p < n and not isVowel(s[p]):
                p += 1
            while q > 0 and not isVowel(s[q]):
                q -= 1

            if p < q:
                s[q], s[p] = s[p], s[q]
                p += 1
                q -= 1
        return "".join(s)