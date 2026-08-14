class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=[0]
        sum_ = 0
        for i in nums:
            sum_+=i
            l.append(sum_)
        for i in range(len(nums)):
            if l[i]==l[len(nums)]-l[i+1]:
                return i
        return -1

        