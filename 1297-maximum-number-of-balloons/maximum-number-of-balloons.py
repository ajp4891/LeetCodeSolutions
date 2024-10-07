class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = "balloon"
        bdic = defaultdict(int)

        for c in balloon:
            bdic[c] += 1

        ans = float('inf')

        for l, cnt in bdic.items():
            tcnt = text.count(l)
            ans = min(ans, (tcnt // cnt))

        return ans