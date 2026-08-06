class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_ = sum(arr[:k])
        i=0
        j=k
        avg = sum_/k
        if avg >= threshold:
            s =1
        else:
            s=0
        while j<len(arr):
            sum_ = sum_-arr[i]+arr[j]
            avg = sum_/k
            if avg>=threshold:
               s+=1
            i+=1
            j+=1
        return s

        