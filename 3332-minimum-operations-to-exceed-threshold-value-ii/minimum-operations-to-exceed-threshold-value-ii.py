class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op = 0

        while nums and len(nums) >= 2 and nums[0] < k:
            # print("Before", nums)
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            op += 1
            # print("-->", op, " After", nums)

        if not nums or nums[0] < k:
            return 0

        return op