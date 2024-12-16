class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for i, n in enumerate(nums):
            heapq.heappush(heap, (n, i))

        for _ in range(k):
            n, i = heapq.heappop(heap)
            n *= multiplier
            heapq.heappush(heap, (n, i))
            nums[i] = n

        return nums
