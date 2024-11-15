class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return len(set(candies))
        if len(candies) <= k:
            return 0
        l, r, n = 0, 0, len(candies)

        counter = Counter(candies)
        ans = 0
        while r < k:
            if counter[candies[r]] == 1:
                del counter[candies[r]]
            else:
                counter[candies[r]] -= 1
            r += 1

        ans = len(counter)

        while r < n:
            if counter[candies[r]] == 1:
                del counter[candies[r]]
            else:
                counter[candies[r]] -= 1
            r += 1

            counter[candies[l]] += 1
            l += 1
            ans = max(ans, len(counter))

        return ans
