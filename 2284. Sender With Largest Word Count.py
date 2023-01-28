class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dictionary = {}
        maxs = set()
        for i in range(len(senders)):
            if senders[i] not in dictionary:
                dictionary[senders[i]] = len(messages[i].split())
                maxs.add(len(messages[i].split()))
            else:
                dictionary[senders[i]] += len(messages[i].split())
                maxs.add(dictionary[senders[i]])
        
        a = []
        m = max(maxs)
        for i in dictionary:
            if dictionary[i] == m:
                a.append(i)

        a = sorted(a)
        return a[-1]
