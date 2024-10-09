import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # final = []
        # for n in nums:
        #     sq = n * n
        #     i = bisect.bisect_left(final, sq)
        #     final.insert(i, sq)

        # return final

        i = 0
        n = len(nums)
        j = n - 1
        ans = [0] * n
        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                ans[k] = nums[i] ** 2
                i += 1
            else:
                ans[k] = nums[j] ** 2
                j -= 1

        return ans