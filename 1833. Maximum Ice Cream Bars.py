class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0

        for i in costs:
            if i <= coins:
                coins -= i
                count += 1
            else:
                break
        return count
