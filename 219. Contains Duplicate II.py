class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        obj = {}
        j = 0
        for i in nums:
            if i not in obj:
                obj[i] = j
            else:
                if abs(obj[i]-j) <= k:
                    return True
                else:
                    obj[i] = j
            j += 1
        return False
    
