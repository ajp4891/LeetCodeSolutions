class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def dfs(nums, i, curorval, target):
            if i == len(nums):
                if curorval == target:
                    return 1
                return 0

            withoutc = dfs(nums, i + 1, curorval, target)
            withc = dfs(nums, i + 1, curorval | nums[i], target)

            return withoutc + withc


        maxorval = 0
        for n in nums:
            maxorval |= n

        return dfs(nums, 0, 0, maxorval)