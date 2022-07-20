class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 56 题写法
        #         intervals.append(newInterval)
        #         intervals.sort(key=lambda x: x[0])
        #         merge = []

        #         for i in range(len(intervals)):
        #             if not merge or intervals[i][0] > merge[-1][1]:
        #                 merge.append(intervals[i])
        #             else:
        #                 merge[-1][1] = max(merge[-1][1], intervals[i][1])
        #         return merge

        #         # 二分法查找端点
        #         L, R = newInterval
        #         # 二分查找（左），参考bisect.bisect_left
        #         pL, r = 0, len(intervals)
        #         while(pL<r):
        #             m = (pL+r)//2
        #             if intervals[m][1]<L: pL = m+1
        #             else: r = m
        #         # 二分查找（右），参考bisect.bisect_right
        #         pR, r =  pL, len(intervals)
        #         while(pR<r):
        #             m = (pR+r)//2
        #             if intervals[m][0]>R: r = m
        #             else: pR = m+1

        #         # python slice替换，待替换片段和原片段等长时，时间复杂度为O(R-L), 否则为O(N-L)
        #         intervals[pL:pR] = [newInterval] if pL==pR else [[min(L, intervals[pL][0]), max(R, intervals[pR-1][1])]]
        #         return intervals

        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])
        return ans