class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        min_val = float('inf')
        negatives = 0

        for row in matrix:
            for val in row:
                total += abs(val)
                if val < 0:
                    negatives += 1
                
                if abs(val) < min_val:
                    min_val = abs(val)

        if negatives % 2 != 0:
            total -= 2 * min_val

        return total