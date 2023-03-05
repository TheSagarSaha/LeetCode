class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rowZeros = set()
        colZeros = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rowZeros.add(row)
                    colZeros.add(col)
        
        for row in range(len(matrix)):
            if row in rowZeros:
                matrix[row] = [0]*len(matrix[row])
            
            for col in range(len(matrix[row])):
                if col in colZeros:
                    matrix[row][col] = 0
        
        
