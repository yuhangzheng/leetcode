class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            if not merge or intervals[i][0] > merge[-1][1]:
                merge.append(intervals[i])
            else:
                merge[-1][1] = max(merge[-1][1], intervals[i][1])
        return merge