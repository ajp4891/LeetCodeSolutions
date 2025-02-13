class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op = 0

        num = heapq.heappop(nums)

        while num < k:
            num = heapq.heappushpop(nums, num * 2 + heapq.heappop(nums))
            op += 1

        return op