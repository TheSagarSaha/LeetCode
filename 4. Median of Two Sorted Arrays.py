class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1+nums2
        arr.sort()
        l = len(arr)
        if l % 2 != 0:
            return arr[l//2]
        
        ans = arr[(l//2)-1] + arr[(l//2)]
        return ans/2
