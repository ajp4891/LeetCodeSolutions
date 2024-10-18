class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        max_stolen = 0
        dp = {}
        def dfs(current_house, stole_so_far):
            if current_house >= n:
                return stole_so_far

            if current_house in dp:
                return dp[current_house]
            
            skip = dfs(current_house + 1, stole_so_far)
            current = dfs(current_house + 2, stole_so_far) + nums[current_house]

            dp[current_house] = max(skip, current)
            return dp[current_house]

        return dfs(0, 0)