class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        f_w = s2[:len(s1)]
        d1={}
        for y in f_w:
            if y in d1:
                d1[y]+=1
            else:
                d1[y]=1
        i=0
        j = len(s1)
        d ={}
        for x in s1:
            if x in d:
                d[x]+=1
            else:
                d[x]=1
        if d1 ==d:
            return True
        while j<len(s2):
            d1[s2[i]]-=1
            if d1[s2[i]]==0:
                del d1[s2[i]]
            if s2[j] in d1:
                d1[s2[j]]+=1
            else:
                d1[s2[j]]=1
            if d1==d:
                return True
            i+=1
            j+=1
        return False


        

        