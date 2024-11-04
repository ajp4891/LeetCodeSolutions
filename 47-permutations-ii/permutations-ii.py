class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(index):
            if index == len(nums):
                res.append(nums[:])
                return

            seen = set()

            for i in range(index, len(nums)):
                if nums[i] not in seen:
                    nums[index], nums[i] = nums[i], nums[index]
                    bt(index + 1)
                    nums[i], nums[index] = nums[index], nums[i]
                    seen.add(nums[i])

        bt(0)
        return res