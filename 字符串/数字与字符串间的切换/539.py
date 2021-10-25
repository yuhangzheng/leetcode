class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ms = []
        for t in timePoints:
            h, m = t.split(":")
            ms.append(int(h) * 60 + int(m))
            ms.append(int(h) * 60 + int(m) + 1440)
        ms.sort()
        res = float("inf")
        for i in range(1, len(ms)):
            res = min(res, ms[i] - ms[i - 1])
        return res

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        d = set()
        for c in timePoints:
            k = int(c[: 2]) * 60 + int(c[3: ])
            if k in d:  #可能快在了判重这里
                return 0
            d.add(k)
        d = sorted(d)
        d.append(d[0] + 1440)
        return min(d[i] - d[i - 1] for i in range(1, len(d)))

