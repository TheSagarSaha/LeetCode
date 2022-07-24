class Solution:
    def isValid(self, s: str) -> bool:
        openChars = ['(', '{', '[']
        closeChars = [')', '}', ']']
        count = 0
        if s[0] in closeChars or len(s)%2 != 0:
            return False
        
        res = []
        for i in s:
            if i in openChars:
                ind = openChars.index(i)
                res.insert(count, i)
                res.insert(count+1, closeChars[ind])
            count += 1;
        res = ''.join(res)
        if res == s:
            return True
        return False
    
