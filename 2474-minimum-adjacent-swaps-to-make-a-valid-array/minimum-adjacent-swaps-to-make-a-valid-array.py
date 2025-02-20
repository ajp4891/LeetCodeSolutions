class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_indx =  nums.index(min(nums))
        max_indx =  nums[::-1].index(max(nums))

        ans = min_indx + max_indx
        if min_indx > len(nums) - max_indx - 1:
            ans -= 1

        return ans