class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        li = []
        l = 0
        j = len(p)

        d = {}

        for i in p:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        d1 = {}

        for i in s[:len(p)]:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        if d1 == d:
            li.append(0)

        while j < len(s):
            d1[s[l]] -= 1

            if d1[s[l]] == 0:
                del d1[s[l]]

            if s[j] in d1:
                d1[s[j]] += 1
            else:
                d1[s[j]] = 1

            l += 1
            j += 1

            if d1 == d:
                li.append(l)

        return li