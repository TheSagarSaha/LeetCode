class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = ''
        for word in words:
            for letter in word:
                if chars.count(letter) < word.count(letter):
                    break
            else:
                res += word
        return len(res)
