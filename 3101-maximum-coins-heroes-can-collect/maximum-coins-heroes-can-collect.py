class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        d = sorted(zip(monsters, coins), key=lambda x: x[0])
        coins_sum = [d[0][1]]

        for i, (_, coin) in enumerate(d[1:]):
            coins_sum.append(coins_sum[-1] + coin)

        ans = [0] * len(heroes)
        for i, h in enumerate(heroes):
            l, r = 0, len(d) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if d[mid][0] > h:
                    r = mid - 1
                else:
                    l = mid + 1

            if l == 0 and d[l][0] > h:
                pass
            else:
                ans[i] = coins_sum[r]

        return ans