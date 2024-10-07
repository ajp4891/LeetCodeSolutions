class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        product = 1

        for n in nums:
            if n == 0:
                zeroes += 1
            else:
                product *= n

        ans = []
        if zeroes > 1:
            return [0] * len(nums)
        elif zeroes == 1:
            for n in nums:
                if n == 0:
                    ans.append(product)
                else:
                    ans.append(0)

            return ans

        for n in nums:
            ans.append(product // n)

        return ans