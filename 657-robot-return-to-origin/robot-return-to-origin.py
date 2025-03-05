class Solution:
    def judgeCircle(self, moves: str) -> bool:
        up_down = left_right = 0
        for move in moves:
            if move == "U":
                up_down -= 1
            elif move == "D":
                up_down += 1
            elif move == "L":
                left_right -= 1
            else:
                left_right += 1

        return up_down == left_right == 0