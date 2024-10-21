class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d  = set(nums)
        start = 0
        for n in nums:
            if start not in d:
                return start
            start += 1

        return len(nums)