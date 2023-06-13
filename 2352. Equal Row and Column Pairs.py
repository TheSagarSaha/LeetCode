class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for row in range(len(grid)):
            array = []
            for col in range(len(grid)):
                array.append(grid[col][row])
            for i in range(len(grid)):
                if grid[i] == array:
                    count += 1
        return count
