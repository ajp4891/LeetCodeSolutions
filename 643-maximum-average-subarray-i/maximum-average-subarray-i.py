class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k - 1
        runsum = sum(nums[:k])
        mxavg = runsum / k

        while j < len(nums) - 1:
            runsum -= nums[i]
            i += 1
            j += 1
            runsum += nums[j]
            mxavg = max(mxavg, runsum / k)

        return mxavg