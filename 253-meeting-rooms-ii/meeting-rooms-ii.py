class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        cal = []
        for s, e in intervals:
            cal.append((s, 1))
            cal.append((e, -1))

        cal.sort(key = lambda x: (x[0], x[1]))
        crooms = 0
        for e in cal:
            crooms += e[1]
            rooms = max(crooms, rooms)
        
        return rooms