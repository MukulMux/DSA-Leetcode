#884. Uncommon Words from Two Sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()

        reslist = []

        d = {}
        for i in s1:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for j in s2:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1

        for key, value in d.items():
            if value == 1:
                reslist.append(key)
        return reslist




