class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [False] * len(queries)
        pre = [0] * len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = pre[i - 1]

        for i in range(len(queries)):
            q = queries[i]
            start = q[0]
            end = q[1]
            ans[i] = pre[end] - pre[start] == 0

        return ans