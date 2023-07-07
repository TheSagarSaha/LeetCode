class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, total = float(inf), nums[0]
        left, right = 0, 1
        while left < right:
            if total < target and right < len(nums):
                total += nums[right]
                right += 1
            elif total >= target:
                total -= nums[left]
                
                res = min(res, (right-left))
                left += 1
            else:
                left += 1
        
        if res == float(inf):
            return 0
        return res
