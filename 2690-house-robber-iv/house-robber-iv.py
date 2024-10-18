class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def in_the_range(need):
            count = i = 0
            while i < len(nums):
                if nums[i] <= need:
                    count += 1
                    i += 1
                i += 1
            if count >= k:
                return True
            return False

        minl, maxr = float('inf'), float('-inf')

        for n in nums:
            minl = min(n, minl)
            maxr = max(n, maxr)

        while minl <= maxr:
            mid = minl + (maxr - minl) // 2
            if in_the_range(mid):
                maxr = mid - 1
            else:
                minl = mid + 1

        return minl