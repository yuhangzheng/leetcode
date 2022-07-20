class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # if not s or not g:
        #     return 0
        # g.sort()
        # s.sort()
        # j = len(s) -1
        # count = 0

        # for i in range(len(g)-1, -1, -1):
        #     if s[j] >= g[i]:
        #         count += 1
        #         if j == 0:
        #             return count
        #         else:
        #             j -= 1
        # return count
        g.sort()
        s.sort()
        n, m = len(g), len(s)
        i = j = count = 0

        while i < n and j < m:
            while j < m and g[i] > s[j]:
                j += 1
            if j < m:
                count += 1
            i += 1
            j += 1

        return count