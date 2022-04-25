class Solution:
    def leastBricks(self, wall):
        ret = len(wall)
        d = {}
        for li in wall:
            for i in range(len(li) - 1):
                if i != 0:
                    li[i] = li[i - 1] + li[i]
                d[li[i]] = d.get(li[i], 0) + 1
        return ret-max(d.values()) if d else ret
