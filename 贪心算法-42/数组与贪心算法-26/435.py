class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #         # 动规
        #         if not intervals:
        #             return 0

        #         intervals.sort()
        #         n = len(intervals)
        #         f = [1]

        #         for i in range(1, n):
        #             f.append(max((f[j] for j in range(i) if intervals[j][1] <= intervals[i][0]), default=0) + 1)

        #         return n - max(f)

        # 贪心
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]
        ans = 1

        for i in range(1, n):
            if intervals[i][0] >= right:
                ans += 1
                right = intervals[i][1]

        return n - ans