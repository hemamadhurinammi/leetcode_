class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c =0
        l=0
        j =k
        for i in range(k):
            if s[i] in "aeiou":
                c+=1
        max_ = c
        while j< len(s):
            if s[l] in "aeiou":
                c-=1
            if s[j] in "aeiou":
                c+=1
            l+=1
            j+=1
            max_ = max(max_,c)
        return max_
            


        