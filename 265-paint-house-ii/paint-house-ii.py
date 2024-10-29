class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        total_houses = len(costs)
        if total_houses == 1:
            return min(costs[0])

        ans = float('inf')
        dp = dict()

        def dfs(totalCost, houseId, prev_colorId):
            if houseId >= total_houses:
                return totalCost

            if (houseId, prev_colorId) in dp:
                return dp[(houseId, prev_colorId)]
        
            dp[(houseId, prev_colorId)] = float('inf')
        
            for i, color in enumerate(costs[houseId]):
                if i != prev_colorId or houseId == 0:
                    cost = dfs(totalCost, houseId + 1, i) + color
                    dp[(houseId, prev_colorId)] = min(dp[(houseId, prev_colorId)], cost)

            return dp[(houseId, prev_colorId)]

        return dfs(0, 0, 0)