class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in image:
            arr = i
            arr = arr[::-1]
            for j in range(len(arr)):
                if arr[j] == 0:
                    arr[j] = 1
                else:
                    arr[j] = 0
            res.append(arr)
        return res
