class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph += "."
        res = 0
        ans = ""
        banned = set(banned)
        wordSet = {}
        seperator = {"!", "?", "'", ",", ";", ".", " "}
        string = ""
        for i in paragraph.lower():
            if i not in seperator:
                string += i
            else:
                if string not in banned and string in wordSet and string != "":
                    wordSet[string] += 1
                elif string not in banned and string not in wordSet and string != "":
                    wordSet[string] = 1
                if string not in banned and string != "" and wordSet[string] > res:
                    res = wordSet[string]
                    ans = string
                string = ""
        return ans
