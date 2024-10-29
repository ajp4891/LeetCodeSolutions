class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # current_zeros = 0
        # maxones = 0
        # ones = 0
        # i = j = 0
        # while j < len(nums):
        #     if nums[j] == 0:
        #         if k == 0:
        #             ones = -1
        #             i = j
                
        #         if current_zeros == k:
        #             while i < j:
        #                 ones -= 1
        #                 if nums[i] == 0:
        #                     break
        #                 i += 1
        #             current_zeros -= 1
        #             i += 1
        #         current_zeros += 1

        #     ones += 1                
        #     maxones = max(ones, maxones)
        #     j += 1

        # return maxones
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1