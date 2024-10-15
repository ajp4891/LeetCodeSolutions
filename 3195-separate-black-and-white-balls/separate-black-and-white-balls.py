class Solution:
    def minimumSteps(self, s: str) -> int:
        whitepos = 0
        swaps = 0

        for cpos, c in enumerate(s):
            if c == "0":
                swaps += cpos - whitepos
                whitepos += 1

        return swaps