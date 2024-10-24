class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target <= nums[-1] else 1

        l, r = 0, len(nums)            
        while l < r:
            m = l + (r - l) // 2
            if target <= nums[m]:
                r = m
            else:
                l = m + 1

        return (l )