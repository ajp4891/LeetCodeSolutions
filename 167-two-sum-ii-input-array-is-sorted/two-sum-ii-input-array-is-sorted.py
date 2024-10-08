class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            csum = numbers[i] + numbers[j]
            if csum == target:
                return [i + 1, j + 1]
            
            if target < csum:
                j -= 1
            else:
                i += 1

        return 