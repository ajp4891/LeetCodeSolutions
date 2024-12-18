class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, n in enumerate(prices):
            while stack and  n <= prices[stack[-1]]:
                prices[stack.pop()] -= n
            stack.append(i)
        return prices