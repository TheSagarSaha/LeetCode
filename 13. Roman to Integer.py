class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 
                  'XL':40, 'XC':90, 'CD':400, 'CM':900}
        ind, res = 0, 0
        while ind < len(s):
            if ind+1 < len(s) and s[ind:ind+2] in romans:
                res += romans[s[ind:ind+2]]
                ind += 2
            else:
                res += romans[s[ind]]
                ind += 1
        return res
 
