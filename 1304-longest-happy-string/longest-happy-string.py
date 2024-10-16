class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        happy = []

        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, "a"))
        if b > 0:
            heapq.heappush(heap, (-b, "b"))
        if c > 0:
            heapq.heappush(heap, (-c, "c"))

        while heap:
            # popfirst item
            cnt, c = heapq.heappop(heap)
            cnt = -cnt
            
            if (len(happy) >= 2
                and happy[-1] == c and happy[-2] == c):
                if not heap:
                    break
                
                tmpcnt, tmpc = heapq.heapreplace(heap, (-cnt, c))
                happy.append(tmpc)
                if tmpcnt + 1 < 0:
                    heapq.heappush(heap, (tmpcnt + 1, tmpc))
            else:
                cnt -= 1
                happy.append(c)
                if cnt > 0:
                    heapq.heappush(heap, (-cnt, c))

        return ''.join(happy)