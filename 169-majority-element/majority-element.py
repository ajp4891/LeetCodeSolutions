class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        majority = 1

        for n in nums[1:]:
            print(n, major, majority)
            if n == major:
                majority += 1
            else:
                majority -= 1
                if majority <= 0:
                    major = n
                    majority = 1
            print(n, major, majority)
            print("-------")
        return major