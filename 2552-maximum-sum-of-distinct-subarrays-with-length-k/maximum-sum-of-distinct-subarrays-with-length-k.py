class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        maxsum = 0

        start, end = 0, 0
        runningsum = 0

        while end < k:
            counter[nums[end]] += 1
            runningsum += nums[end]
            end += 1

        if len(counter) == k:
            maxsum = runningsum

        while end < len(nums):
            counter[nums[start]] -= 1
            if counter[nums[start]] == 0:
                del counter[nums[start]]
            runningsum -= nums[start]
            start += 1
            
            counter[nums[end]] += 1
            runningsum += nums[end]
            end += 1

            if len(counter) == k and runningsum > maxsum:
                maxsum = runningsum

        return maxsum