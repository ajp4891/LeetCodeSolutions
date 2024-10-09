import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        final = []
        for n in nums:
            sq = n * n
            i = bisect.bisect_left(final, sq)
            final.insert(i, sq)

        return final