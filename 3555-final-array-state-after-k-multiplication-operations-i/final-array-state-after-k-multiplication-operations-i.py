class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for i, n in enumerate(nums):
            heapq.heappush(heap, (n, i))

        for _ in range(k):
            _, i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap, (nums[i], i))

        return nums
