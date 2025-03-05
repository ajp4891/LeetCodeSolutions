class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_cntr = Counter(moves)

        return move_cntr["U"] == move_cntr["D"] and move_cntr["L"] == move_cntr["R"]
        # up_down = left_right = 0
        # for move in moves:
        #     if move == "U":
        #         up_down -= 1
        #     elif move == "D":
        #         up_down += 1
        #     elif move == "L":
        #         left_right -= 1
        #     else:
        #         left_right += 1

        # return up_down == left_right == 0