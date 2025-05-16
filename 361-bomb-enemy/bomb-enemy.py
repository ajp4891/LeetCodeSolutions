class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])

        max_cnt = 0
        row_kills = 0
        col_kills = [0] * cols

        for row in range(0, rows):
            for col in range(0, cols):
                if col == 0 or grid[row][col - 1]  == 'W':
                    row_kills = 0

                    for k in range(col, cols):
                        if grid[row][k] == 'W':
                            break
                        elif grid[row][k] == 'E':
                            row_kills += 1

                if row == 0 or grid[row - 1][col] == 'W':
                    col_kills[col] = 0
                    for k in range(row, rows):
                        if grid[k][col] == 'W':
                            break
                        elif grid[k][col] == 'E':
                            col_kills[col] += 1

                if grid[row][col] == '0':
                    total_hits = row_kills + col_kills[col]
                    max_cnt = max(max_cnt, total_hits)

        return max_cnt