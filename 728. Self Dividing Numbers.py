class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        arr = []
        for i in range(left, right+1):
            add = True
            for j in str(i):
                if not (int(j) != 0 and i % int(j) == 0):
                    add = False
                    break
            if add:
                arr.append(i)
        # print(arr)
        return arr
