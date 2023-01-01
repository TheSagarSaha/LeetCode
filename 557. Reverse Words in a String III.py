class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        count = 0
        for i in s:
            s[count] = i[::-1]
            count += 1
        return " ".join(s)
