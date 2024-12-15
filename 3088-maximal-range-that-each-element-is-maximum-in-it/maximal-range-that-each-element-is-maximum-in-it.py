class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [0] * n
        r = [0] * n
        stack = []

        for c_idx in range(n):
            while stack and nums[stack[-1]] < nums[c_idx]:
                stack.pop()
            l[c_idx] = -1 if not stack else stack[-1]
            stack.append(c_idx)

        stack = []

        for curr_idx in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[curr_idx]:
                stack.pop()
            r[curr_idx] = n if not stack else stack[-1]
            stack.append(curr_idx)

        ans = [0] * n
        for curr_idx in range(n):
            ans[curr_idx] = r[curr_idx] - l[curr_idx] - 1

        return ans