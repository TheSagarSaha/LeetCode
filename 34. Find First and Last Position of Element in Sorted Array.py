class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid+1
            elif nums[mid] == target:
                start, end = mid, mid
                while start - 1 >= 0 and nums[start - 1] == target:
                    start -= 1
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                return [start, end]
        return [-1, -1]
        
