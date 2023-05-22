class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        res = 0
        while right < len(prices):
            if prices[right] <= prices[left]:
                left = right
                right += 1
            else:
                res = max(res, prices[right] - prices[left])
                right += 1
        return res
