class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = defaultdict(int)
        m, n = len(grid), len(grid[0])
        directions = [(-1, 1), (0, 1), (1, 1)]

        def dfs(r, c, prev_val):
            if not 0 <= r < m or not 0 <= c < n:
                return 0

            if prev_val >= grid[r][c]:
                return 0

            if (r, c) in dp:
                return dp[(r,c)]

            maxval = 0
            for dr, dc in directions:
                val = dfs(r + dr, c + dc, grid[r][c])
                maxval = max(maxval, val)
            dp[(r, c)] = maxval + 1
            return dp[(r, c)]


        maxans = 0
        row = 0
        while row < m:
            for dr, dc in directions:
                maxans = max(maxans, dfs(row + dr, dc, grid[row][0]))
            row += 1

        return maxans
