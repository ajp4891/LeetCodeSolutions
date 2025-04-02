class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        n = len(nums)
        res, i_max, i_j_diff_max = 0, 0, 0
        for k in nums:
            res = max(res, i_j_diff_max * k)
            i_j_diff_max = max(i_j_diff_max, i_max - k)
            i_max = max(i_max, k)

        return res
