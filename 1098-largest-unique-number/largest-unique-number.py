class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        viewed = Counter(nums)
        maxn = -1

        for n, c in viewed.items():
            if c == 1:
                maxn = max(maxn, n)

        return maxn