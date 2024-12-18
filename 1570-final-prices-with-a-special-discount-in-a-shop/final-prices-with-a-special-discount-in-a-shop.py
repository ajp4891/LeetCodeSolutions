class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, n in enumerate(prices):
            if not stack:
                stack.append(i)
                continue
            while stack and  n <= prices[stack[-1]]:
                prices[stack[-1]] -= n
                stack.pop()

            stack.append(i)
        return prices