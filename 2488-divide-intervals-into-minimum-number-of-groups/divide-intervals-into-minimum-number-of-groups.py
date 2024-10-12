class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        min_heap = []
        intervals.sort(key=lambda x: x[0])

        for s, e in intervals:
            if min_heap and min_heap[0] < s:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, e)

        return len(min_heap)