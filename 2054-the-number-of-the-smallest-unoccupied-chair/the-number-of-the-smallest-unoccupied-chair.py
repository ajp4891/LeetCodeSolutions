class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []

        for i, (start, end) in enumerate(times):
            events.append((start, -1, i))
            events.append((end, 1, i))

        events.sort(key=lambda x: (x[0], -x[1]))
        # print(events)

        q = []
        d = {}
        newchair = -1
        lastchairused = -1
        for _, e, fno in events:
            if e == -1:
                if not q:
                    newchair += 1
                    lastchairused = newchair
                    d[fno] = newchair
                else:
                    emptychair = heapq.heappop(q)
                    d[fno] = emptychair
                    lastchairused = emptychair
            else:
                emptychair = d[fno]
                heapq.heappush(q, emptychair)
                del d[fno]

            if fno == targetFriend:
                break
        
        return lastchairused