class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        res = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        
        i = 0
        while i < len(nums) / 2:
            res.append(even[i])
            res.append(odd[i])
            i += 1
        
        return res
