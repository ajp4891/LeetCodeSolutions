class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxcap = 0
        while l < r:
            ccap = (min(height[l], height[r]) * (r - l))
            maxcap = max(maxcap, ccap)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxcap