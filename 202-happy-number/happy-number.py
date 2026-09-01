def sa(n):
    sum =0
    while n>0:
        r = n%10
        sum = sum +r**2
        n = n//10
    return sum
class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            if n<10:
                break
            n = sa(n)
        if n==1 or n==7:
            return True
        else:
            return False
        

       


        