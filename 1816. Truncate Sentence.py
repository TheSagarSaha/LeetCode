class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        arr = []
        for i in range(k):
            arr.append(s[i])

        return " ".join(arr)
