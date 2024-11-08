class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        e = (1 << maximumBit) - 1
        for i in range(1, len(nums)):
            nums[i] ^= nums[i-1]

        ans = []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(e ^ nums[i])

        return ans