class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, n in enumerate(prices):
            if not stack:
                stack.append((n, i))
                continue
            # print(i, stack, prices)
            while stack:
                if n <= stack[-1][0]:
                    prices[stack[-1][1]] -= n
                    stack.pop()
                else:
                    break

            stack.append((n, i))
            # print(i, stack, prices)

        return prices