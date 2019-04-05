# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # Solution 1 - Sort
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # intervals = sorted(intervals, key=lambda x: x.start)
        # in-place sort --> O(1) space complexity
        intervals.sort(key=lambda x: x.start)
        merged = []
        for interval in intervals:
            # merged is empty or the last interval in the merge not cover the interval
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:  # overlap, just need to check the end point.
                merged[-1].end = max(interval.end, merged[-1].end)

        return merged

    # TODO: Solution 2 - Connected Components
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        pass
