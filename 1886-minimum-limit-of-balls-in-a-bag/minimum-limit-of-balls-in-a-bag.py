class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        total = sum(nums)
        num_groups = maxOperations + len(nums)

        if num_groups >= total:
            return 1

        l = 1
        r = max(nums)

        def possible_to_split(m):
            total_op = 0
            for n in nums:
                op = math.ceil(n / m) - 1
                total_op += op
            
            return total_op <= maxOperations

        
        while l < r:
            m = l + ((r - l) // 2)
            if possible_to_split(m):
                r = m
            else:
                l = m + 1

        return l