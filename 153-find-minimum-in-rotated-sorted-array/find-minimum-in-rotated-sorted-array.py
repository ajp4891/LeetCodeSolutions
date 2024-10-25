class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            m = l + (r - l) // 2
            if m > 0 and nums[m] < nums[m - 1]:
                return nums[m]
            if m < len(nums) - 1 and nums[m] > nums[m + 1]:
                return nums[m + 1]

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m

        return nums[l]