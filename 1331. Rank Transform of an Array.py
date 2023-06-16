class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap, res = {}, []
        sortedArr, count = sorted(set(arr)), 1
    
        for i in sortedArr:
            hashmap[i] = count
            count += 1    
        for i in arr:
            res.append(hashmap[i])
        
        return res
