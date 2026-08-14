class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix =[0]
        sum_ =0
        for i in nums:
            sum_+=i
            prefix.append(sum_)
        for i in range(len(nums)):
            if prefix[i]==prefix[len(nums)]-prefix[i+1]:
                return i
        return -1

        

    
        
        