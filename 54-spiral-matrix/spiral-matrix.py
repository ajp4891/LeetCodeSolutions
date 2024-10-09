class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # res = []
        # if not matrix or not matrix[0]:
        #     return res

        # m, n = len(matrix), len(matrix[0])
        # t, b, l, r = 0, m - 1, 0, n - 1

        # while t <= b and l <= r:
        #     # right
        #     for i in range(l, r + 1):
        #         res.append(matrix[t][i])
        #     t += 1

        #     # bottom
        #     for i in range(t, b + 1):
        #         res.append(matrix[i][r])
        #     r -= 1

        #     # left
        #     if t <= b:
        #         for i in range(r, l - 1, -1):
        #             res.append(matrix[b][i])
        #         b -= 1

        #     # top
        #     if l <= r:
        #         for i in range(b, t - 1, -1):
        #             res.append(matrix[i][l])
        #         l += 1

        # return res

        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        arr = []
        rows, cols = len(matrix), len(matrix[0])
        x = y = 0
        direction = 0
        for _ in range(rows*cols):
            arr.append(matrix[x][y])
            visited.add((x,y))

            dx, dy = x + moves[direction][0], y + moves[direction][1]
            if dx == rows or dx == -1 or dy == cols or dy == -1 or (dx, dy) in visited:
                direction = (direction+1)%4
    
            x, y = x + moves[direction][0], y + moves[direction][1]
        return arr