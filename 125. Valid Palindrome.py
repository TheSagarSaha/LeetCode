class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        text = ""
        alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in s:
            if i in alphanumeric:
                text += i
        
        return text == text[::-1]
    
