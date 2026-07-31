class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right = len(numbers)-1
        l=[]
        while left<right:
            s = numbers[left]+numbers[right]
            if s==target:
                l.append(left+1)
                l.append(right+1)
                return l
            elif s>target:
                right-=1
            else:
                left+=1



        