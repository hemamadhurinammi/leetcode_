class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        f_window = blocks[:k]
        i=0
        j=k
        min_ = 0
        for x in range(len(f_window)):
            if blocks[x]=='W':
                min_+=1
        c=min_
        while j<len(blocks):
            if blocks[i]=='W':
                c-=1
            if blocks[j]=='W':
                c+=1
            i+=1
            j+=1
            min_ = min(min_,c)
        return min_
                

                


            



        