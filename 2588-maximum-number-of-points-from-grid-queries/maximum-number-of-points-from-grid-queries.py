class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] # b, r, t, l
        k = len(queries)

        ans = [0] * k

        queries_sorted = [[queries[i], i] for i in range(k)]
        queries_sorted.sort()
        

        visited = {(0, 0)}
        q = [[grid[0][0], 0, 0]]
        score = 0
        prev_query = -1

        for a, ind in queries_sorted:
            if prev_query == a:
                ans[ind] = score

            while q and q[0][0] < a:
                score += 1
                _, i, j = heapq.heappop(q)
                
                for di, dj in directions:
                    i2 = di + i
                    j2 = dj + j
                    if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]):
                        if (i2, j2) not in visited:
                            heapq.heappush(q, [grid[i2][j2], i2, j2])
                            visited.add((i2, j2))

            ans[ind] = score
            prev_query = a


        return ans