class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]

        def swap_pos(state, i, j):
            s = list(state)
            s[i], s[j] = s[j], s[i]
            return ''.join(s)

        target = "123450"
        start = ''.join(str(n) for r in board for n in r)

        visited = set()
        q = deque([start])
        visited.add(start)

        counts = 0

        while q:
            for _ in range(len(q)):
                curr_board = q.popleft()

                if curr_board == target:
                    return counts

                pos_of_zero = curr_board.index('0')
                for new_zero_pos in directions[pos_of_zero]:
                    next_board = swap_pos(curr_board, pos_of_zero, new_zero_pos)

                    if next_board in visited:
                        continue

                    visited.add(next_board)
                    q.append(next_board)
            counts += 1

        return -1