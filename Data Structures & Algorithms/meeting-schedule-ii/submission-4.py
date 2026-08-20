"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        res = -float('inf')
        intervals.sort(key = lambda x : x.start)

        meeting_end_time =[]

        for meet in intervals:
            if meeting_end_time and meeting_end_time[0]<=meet.start:
                heapq.heappop(meeting_end_time)

            heapq.heappush(meeting_end_time,meet.end)

        return len(meeting_end_time)



        
        
        