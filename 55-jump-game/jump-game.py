class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        n = len(nums) - 1

        for i in nums[1:]:
            if jump <= 0:
                return False
            
            if jump >= n:
                break

            jump = max(jump - 1, i)
            
        return True