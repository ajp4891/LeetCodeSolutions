class Solution:
    def jump(self, nums: List[int]) -> int:
        end = far = ans = 0
        n = len(nums)
        for i in range(n - 1):
            if far < nums[i] + i:
                far = nums[i] + i

            if i == end:
                end = far
                ans += 1

        return ans