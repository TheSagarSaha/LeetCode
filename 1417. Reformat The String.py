class Solution:
    def reformat(self, s: str) -> str:
        nums = set("1234567890")
        numCount, charCount = [], []
        for i in s:
            if i not in nums:
                charCount.append(i)
            else:
                numCount.append(i)
        
        if len(s) % 2 == 0:
            if len(charCount) != len(numCount):
                return ""
            
            res = ""
            for i in range(len(charCount)):
                res += charCount[i] + numCount[i]
            return res
        
        if (len(charCount) + 1 == len(numCount)):
            res = numCount[0]
            for i in range(len(charCount)):
                res += charCount[i] + numCount[i+1]
            return res
        elif (len(charCount) - 1 == len(numCount)):
            res = charCount[0]
            for i in range(len(numCount)):
                res += numCount[i] + charCount[i+1]
            return res
        
        return ""
