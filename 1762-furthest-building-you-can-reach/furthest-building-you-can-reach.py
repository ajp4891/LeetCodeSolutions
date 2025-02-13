class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minheap = []

        prev_h = heights[0]
        for i, h in enumerate(heights[1:]):
            diff = prev_h - h
            prev_h = h
            if diff < 0:
                heapq.heappush(minheap, -diff)
                if ladders > 0:
                    ladders -= 1
                elif bricks == 0:
                    return i
                else:
                    usebricks = heapq.heappop(minheap)
                    bricks -= usebricks
                    if bricks < 0:
                        return i

        return len(heights) - 1