class Solution:
    def canSortArray(self, nums):
        min_prev = nums[0]
        max_prev = nums[0]
        max_prev_prev = float('-inf')
        set_bits = bin(nums[0]).count("1")

        for i in range(1, len(nums)):
            if bin(nums[i]).count("1") == set_bits:
                max_prev = max(max_prev, nums[i])
                min_prev = min(min_prev, nums[i])
            else:
                if min_prev < max_prev_prev:
                    return False

                max_prev_prev = max_prev
                max_prev = nums[i]
                min_prev = nums[i]
                set_bits = bin(nums[i]).count("1")

        if min_prev < max_prev_prev:
            return False

        return True