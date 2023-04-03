class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for i in emails:
            email = i.split("@")
            name = ""
            for j in email[0]:
                if j == "+":
                    break
                elif j != ".":
                    name += j
            s.add(name+"@"+email[1])
        return len(s)
