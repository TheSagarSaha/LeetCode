class Solution:
    def isPalindrome(self, x: int) -> bool:
        text = str(x)
        string = ""
        for i in text:
            string = i + string
        
        if string == text:
            return True
        else:
            return False
            
