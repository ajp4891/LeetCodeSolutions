class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        STONE = "#"
        EMPTY = "."
        OBSTACLE = "*"

        m, n = len(box), len(box[0])
        if m == 1 and n == 1:
            return box

        res = [["."] * m for _ in range(n)]

        for row in range(m):
            current_empty = n - 1
            for col in range(n - 1, -1, -1):
                if box[row][col] == STONE:
                    res[current_empty][m - row - 1] = STONE
                    current_empty -= 1
                elif box[row][col] == OBSTACLE:
                    current_empty = col
                    res[current_empty][m - row - 1] = OBSTACLE
                    current_empty -= 1

        return res
                