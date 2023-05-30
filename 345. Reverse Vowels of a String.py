class Solution:
    def reverseVowels(self, s: str) -> str:
        res = [" "] * len(s)
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] in vowels and s[right] in vowels:
                res[left] = s[right]
                res[right] = s[left]
                left += 1
                right -= 1
            elif s[left] in vowels and s[right] not in vowels:
                res[right] = s[right]
                right -= 1
            elif s[left] not in vowels and s[right] in vowels:
                res[left] = s[left]
                left += 1
            else:
                res[left] = s[left]
                res[right] = s[right]
                right -= 1
                left += 1
        return "".join(res)
                
