class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k
        nums.sort(reverse=True)  # Start with the largest number for efficiency

        if nums[0] > target_sum:
            return False

        # Backtracking helper function
        def backtrack(index, subset_sums):
            if index == len(nums):
                # return all(s == target_sum for s in subset_sums)
                return sum(subset_sums) == total_sum
            
            num = nums[index]
            for i in range(k):
                if subset_sums[i] + num <= target_sum:
                    subset_sums[i] += num
                    if backtrack(index + 1, subset_sums):
                        return True
                    subset_sums[i] -= num
                if subset_sums[i] == 0:
                    break  # Avoid duplicate work
                
            return False

        return backtrack(0, [0] * k)