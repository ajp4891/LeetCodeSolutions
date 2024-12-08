class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        heap = []

        events.sort()

        maxv = 0
        ans = 0

        for e in events:
            while heap and heap[0][0] < e[0]:
                maxv = max(maxv, heap[0][1])
                heapq.heappop(heap)

            ans = max(ans, maxv + e[2])

            heapq.heappush(heap, (e[1], e[2]))

        return ans