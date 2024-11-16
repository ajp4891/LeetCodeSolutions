class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        n = len(nums)
        res = [-1] * (n - k + 1)

        counter = 1
        i = 1
        while i < n:
            if nums[i] == nums[i - 1] + 1:
                counter += 1
            else:
                counter = 1

            if counter >= k:
                res[i - k + 1] = nums[i]
            i += 1
        return res