class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #### Inbuilt Reverse + Transpose
        matrix.reverse()
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #### Replace by indices
        # n = len(matrix)
        # for off in range(n // 2):
        #     for ind in range(off, n - off - 1):
        #         matrix[off][ind], \
        #             matrix[n - ind - 1][off], \
        #                 matrix[n - off - 1][n - ind - 1], \
        #                     matrix[ind][n - off - 1] \
        #                     = \
        #         matrix[n - ind - 1][off], \
        #             matrix[n - off - 1][n - ind - 1], \
        #                 matrix[ind][n - off - 1], \
        #                     matrix[off][ind]


        #### Manual reverse + Transpose
        # n = len(matrix)
        # for i in range(n//2):
        #     matrix[i],matrix[n-i-1] = matrix[n-i-1],matrix[i]
        
        # for i in range(n):
        #     for j in range(i):
        #         matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]