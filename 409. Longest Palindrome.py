class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        res = 0
        for i in c:
            res += int(c[i] / 2) * 2
            if res % 2 == 0 and c[i] % 2 != 0:
                res += 1
        return res
