class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        dict1 = {}
        ans2 = []
        dict2 = {}
        
        for i in nums1:
            if i not in nums2 and i not in dict1:
                ans1.append(i)
                dict1[i] = i
        
        for i in nums2:
            if i not in nums1 and i not in dict2:
                ans2.append(i)
                dict2[i] = i
        
        return [ans1, ans2]
    
