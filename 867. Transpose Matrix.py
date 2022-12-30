class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        j = 0
        while j < len(matrix[0]):
            arr = []
            for i in range(len(matrix)):
                arr.append(matrix[i][j])
            res.append(arr)
            j += 1
        return res 
