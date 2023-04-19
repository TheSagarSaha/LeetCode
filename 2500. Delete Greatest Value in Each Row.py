class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res, m, n = 0, 0, len(grid)
        arr = []
        while grid[len(grid)-1]:
            arr.append(max(grid[m]))
            grid[m].remove(max(grid[m]))
            m += 1

            if m == n:
                res += max(arr)
                arr = []
                m = 0

        return res
