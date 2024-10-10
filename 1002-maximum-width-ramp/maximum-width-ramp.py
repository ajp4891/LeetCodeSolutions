class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # rmax = list(nums)
        # for i in range(len(nums) - 2, -1, -1):
        #     rmax[i] = max(rmax[i], rmax[i + 1])

        # l = r = 0
        # maxw = 0
        # while r < len(nums):
        #     while l < r and nums[l] > rmax[r]:
        #         l += 1

        #     maxw = max(maxw, r - l)
        #     r += 1
        # return maxw
        stack = []
        res = 0
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:
                stack.append(i)

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                res = max(res, j - stack.pop())

        return res