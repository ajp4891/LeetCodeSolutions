class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xo1, xo2 = 0, 0

        len1, len2 = len(nums1), len(nums2)

        if len2 % 2:
            for num in nums1:
                xo1 ^= num

        if len1 % 2:
            for num in nums2:
                xo2 ^= num

        return xo1 ^ xo2