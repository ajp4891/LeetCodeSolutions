class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # how permutations work logic,
        # p1 p2 p3 ... pk... pn
        # next permutation will have a common prefix, let's say p1 p2 p3 ... pk-1 now the next term pk will change to the next greater term (greater than pk) available and then the rest of the terms should be arranged in sorted order
        # How to find the k, we want to maximize the size of the common prefix for next permutation, so we want to find the first k for which there is a greater term available, this can be done with a linear scan if pj < pj+1 we have a greater term available otherwise not since pj+1 didn't have a greater term available for itself.
        N = len(nums)
        idx = -1
        # Linear scan from end.
        for i in range(N - 2, -1, -1):
            if nums[i] < nums[i + 1]: 
                idx = i
                break
        # if there is no such index then we will not have any common prefix, the terms should be arranged in sorted order
        if idx == -1: 
            nums.sort()
            return
        
        def swap(idx1, idx2):
            nums[idx1] ^= nums[idx2]
            nums[idx2] ^= nums[idx1]
            nums[idx1] ^= nums[idx2] 

        def findSmallestGreaterThan(idx: int):
            ans = idx + 1
            for i in range(idx + 2, N):
                if nums[i] > nums[idx] and nums[i] <= nums[ans]:
                    ans = i
            return ans
        
        def reverse(idx: int):
            i, j = idx, N - 1
            while i < j:
                swap(i, j)
                i += 1
                j -= 1
            
        newIdx = findSmallestGreaterThan(idx)
        swap(idx, newIdx)
        reverse(idx + 1)
        return