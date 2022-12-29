class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        total = ""
        for i in num:
            total += str(i)
        total = int(total) + k
        arr = []
        for i in str(total):
            arr.append(int(i))
        return arr
