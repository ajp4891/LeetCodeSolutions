class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = l + (r - l) // 2
            timespent = 0

            for banana in piles:
                timespent += math.ceil(banana / mid)

            if timespent <= h:
                r = mid
            else:
                l = mid + 1

        return r