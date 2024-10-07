class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums

        ans = []
        first = last = nums[0]

        for i in nums[1:]:
            if i - 1 != last:
                if first == last:
                    ans.append(str(first))
                else:
                    ans.append(str(first) + "->" + str(last))
                first = i
            last = i

        if first == last:
            ans.append(str(first))
        else:
            ans.append(str(first) + "->" + str(last))
        return ans