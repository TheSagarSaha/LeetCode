class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        res = []
        start, end = nums[0], -1234567890
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                end = nums[i]
            elif end == -1234567890:
                res.append(str(start))
                start = nums[i]
            else:
                res.append(str(start) + "->" + str(end))
                start = nums[i]
                end = -1234567890

            if i+1 == len(nums):
                if end == -1234567890:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
        return res

