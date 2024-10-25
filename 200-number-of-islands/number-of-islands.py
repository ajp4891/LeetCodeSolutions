class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        r, c = len(grid), len(grid[0])
        count = 0
        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if (0 <= x < r) and (0 <= y < c) and grid[x][y] == "1":
                    stack.append((x+1, y))
                    stack.append((x-1, y))
                    stack.append((x, y+1))
                    stack.append((x, y-1))
                    grid[x][y] = "0"

        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1


        return count