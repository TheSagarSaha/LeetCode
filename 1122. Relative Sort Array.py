class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        arr = []
        for i in arr2:
            for j in range(c[i]):
                arr.append(i)
        remaining = list(set(arr1) - set(arr2))
        remaining.sort()
        for i in remaining:
            for j in range(c[i]):
                arr.append(i)
        return arr
        
