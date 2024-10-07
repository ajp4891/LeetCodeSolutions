class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        lowest = nums[0]

        for n in nums[1:]:
            if abs(n) <= abs(lowest):
                if abs(lowest) == abs(n) and n < lowest:
                    continue
                lowest = n

        return lowest