class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1

        events = []

        for s, e in intervals:
            events.append([s, 1])
            events.append([e, -1])

        events.sort(key=lambda x: (x[0], -x[1]))

        maxgroups = 0
        print(events)
        currentgroup = 0

        for t, e in events:
            currentgroup = currentgroup + e
            maxgroups = max(maxgroups, currentgroup)

        return maxgroups