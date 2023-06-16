class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hashmap = {}
        for i in range(len(mat)):
            hashmap[i] = mat[i].count(1)
        
        hashmap = sorted(hashmap.items(), key=lambda item: item[1])
        res = []
        for i in range(k):
            res.append(hashmap[i][0])
        
        return res

#-------------------NOT OPTIMIZED SOLUTION BELOW---------------------------


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rank, arr, res, count = {}, [], [], 0
        for i in mat:
            rank[count] = 0
            count += 1
            arr.append(i.count(1))
        
        for i in range(len(rank)):
            for j in range(len(rank)):
                if i != j and arr[i] < arr[j]:
                    rank[i] -= 1
                elif i < j and arr[i] == arr[j]:
                    rank[i] -= 1
        
        rank = sorted(rank.items(), key=lambda item: item[1])

        for i in range(k):
            res.append(rank[i][0])
        
        return res
