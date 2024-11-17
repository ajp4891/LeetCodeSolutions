class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        total = 0
        ans = float('inf')
        while r < len(nums):
            total += nums[r]
            while total >= target:
                if r - l + 1 < ans:
                    ans = r - l + 1
                total -= nums[l]
                l += 1
            r += 1

        return ans if ans != float('inf') else 0