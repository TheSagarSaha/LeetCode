class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for i in accounts:
            total = 0
            for j in i:
                total += j
            arr.append(total)
        return max(arr)
