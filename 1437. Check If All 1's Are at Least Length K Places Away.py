class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for i in nums:
            if count < k and i == 1:
                return False

            if i == 1:
                count = 0
            else:
                count += 1
            
        return True
