class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1] and intervals[i][1] >= res[-1][-1]:
                res[-1][1] = intervals[i][1]
            elif intervals[i][0] <= res[-1][1] and intervals[i][1] < res[-1][-1]:
                continue
            else:
                res.append(intervals[i])
        return res
