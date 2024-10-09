class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(left: int, curr: List[int]):
            if left == 0 and len(curr) == len(nums):
                res.append(list(curr))
                return

            for i in range(len(nums)):
                cval = nums[i]
                if cval == None:
                    continue
                curr.append(cval)
                nums[i] = None
                backtrack(left - 1, curr)
                nums[i] = cval
                curr.pop()

        backtrack(len(nums), [])
        return res
