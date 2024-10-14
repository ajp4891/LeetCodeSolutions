class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-item for item in nums]
        heapq.heapify(nums)
        score = 0
        for _ in range(k):
            val = -heapq.heappop(nums)
            score += val
            heapq.heappush(nums, -ceil(val / 3))

        return score