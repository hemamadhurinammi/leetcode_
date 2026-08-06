class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        max_average = sum_ / k

        i = 0
        j = k

        while j < len(nums):
            sum_ = sum_ - nums[i] + nums[j]

            average = sum_ / k

            if average > max_average:
                max_average = average

            i += 1
            j += 1

        return max_average