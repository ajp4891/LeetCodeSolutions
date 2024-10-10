class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        d = sorted(zip(monsters, coins), key=lambda x: x[0])
        coins_sum = [0] * len(coins)
        prefix_sum = 0

        for i, (_, coin) in enumerate(d):
            prefix_sum += coin
            coins_sum[i] = prefix_sum

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