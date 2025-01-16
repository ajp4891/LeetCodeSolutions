class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])

        start = (0,0)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    start = (i, j)

        q = deque([start])
        steps = 1

        def is_range_valid(row, col):
            return (0 <= row < rows and 0 <= col < cols and grid[row][col] != "X")

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    newr, newc = r + dr, c + dc
                    
                    if is_range_valid(newr, newc):
                        if grid[newr][newc] == "#":
                            return steps

                        grid[newr][newc] = "X"
                        q.append((newr, newc))

            steps += 1

        return -1