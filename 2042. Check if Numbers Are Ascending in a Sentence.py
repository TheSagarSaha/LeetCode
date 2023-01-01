class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()   
        nums = {"0","1","2","3","4","5","6","7","8","9"}
        arr = []
        for i in s:
            if i[0] in nums:
                arr.append(int(i))
        
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True
