class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = 0
        lenn = len(nums)
        d = dict()

        for i in range(lenn):
            rem = target - nums[i]
            if (rem in d.keys()):
                return [d[rem], i]
            
            d[nums[i]] = i
