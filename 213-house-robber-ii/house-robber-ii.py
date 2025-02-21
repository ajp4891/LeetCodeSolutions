class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_skip_edge(houses):
            h1 = h2 = 0
            for current_h in houses:
                temp = h1
                h1 = max(current_h + h2, h1)
                h2 = temp

            return h1

        return max(rob_skip_edge(nums[:-1]), rob_skip_edge(nums[1:]))