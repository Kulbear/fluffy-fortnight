# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # Solution 1 - Sort
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        attend = []
        for interval in intervals:
            # CRITICAL: must have <= instead of just <
            # it means two consecutive meetings in case attend[-1].end <= interval.start
            if not attend or attend[-1].end <= interval.start:
                attend.append(interval)
            else:
                return False

        return True
