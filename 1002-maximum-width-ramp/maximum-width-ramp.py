class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        rmax = list(nums)
        for i in range(len(nums) - 2, -1, -1):
            rmax[i] = max(rmax[i], rmax[i + 1])

        l = r = 0
        maxw = 0
        while r < len(nums):
            while l < r and nums[l] > rmax[r]:
                l += 1

            maxw = max(maxw, r - l)
            r += 1
        print(rmax)
        return maxw