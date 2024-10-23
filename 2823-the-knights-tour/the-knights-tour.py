class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        def in_range(row, col):
            return (0 <= row < m and 0 <= col < n and ans[row][col] == -1)

        def move_knight(row, col, count):
            if count == m * n:
                return True

            for movr, movc in moves:
                newr, newc = row + movr, col + movc

                if in_range(newr, newc):
                    ans[newr][newc] = count

                    if move_knight(newr, newc, count + 1):
                        return True

                    ans[newr][newc] = -1

            return False

        ans = [[-1] * n for _ in range(m)]

        ans[r][c] = 0
        move_knight(r, c, 1)
        # ans[r][c] = 0
        return ans