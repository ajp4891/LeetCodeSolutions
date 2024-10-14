class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-item for item in nums]
        heapq.heapify(nums)
        score = 0
        for _ in range(k):
            score -= heapq.heappushpop(nums, floor(nums[0]/3))
        return score