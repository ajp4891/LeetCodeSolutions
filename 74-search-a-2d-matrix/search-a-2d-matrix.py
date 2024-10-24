class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mc = len(matrix)
        nc = len(matrix[0])
        l, r = 0, mc * nc - 1
        while l <= r:
            m = l + (r - l) // 2
            m_ele = matrix[m // nc][m % nc]
            if target == m_ele:
                return True

            if target < m_ele:
                r = m - 1
            else:
                l = m + 1

        return False