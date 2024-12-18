class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, n in enumerate(prices):
            if not stack:
                stack.append(i)
                continue
            # print(i, stack, prices)
            while stack:
                if n <= prices[stack[-1]]:
                    prices[stack[-1]] -= n
                    stack.pop()
                else:
                    break

            stack.append(i)
            # print(i, stack, prices)

        return prices