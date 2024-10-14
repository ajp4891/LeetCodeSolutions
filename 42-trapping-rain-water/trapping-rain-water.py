class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        lmax, rmax = height[i], height[j]

        trapped = 0
        
        while i < j:
            if lmax <= rmax:
                trapped += lmax - height[i]
                i += 1
                lmax = max(lmax, height[i])
            else:
                trapped += rmax - height[j]
                j -= 1
                rmax = max(rmax, height[j])
        return trapped