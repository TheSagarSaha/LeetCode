class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        carry = 0;
        while(i>=0):
            if(digits[i] != 9):
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                carry = 1
            
            i -= 1
        
        digits.insert(0,carry)
        return digits
    
