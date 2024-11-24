class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        rown, coln = len(grid), len(grid[0])

        heap = []
        rows = [1] * rown
        cols = [1] * coln

        for i in range(rown):
            for j in range(coln):
                heapq.heappush(heap, (grid[i][j], i, j))

        while heap:
            _, i, j = heapq.heappop(heap)

            val = max(rows[i], cols[j])
            grid[i][j] = val

            rows[i] = val + 1
            cols[j] = val + 1

        return grid