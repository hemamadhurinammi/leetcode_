class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        f_w = nums[:k]
        i = 0
        j = k
        mx = 0
        cur = sum(f_w)

        freq = {}
        for x in f_w:
            freq[x] = freq.get(x, 0) + 1

        if len(freq) == k:
            mx = cur

        while j < len(nums):
            cur = cur - nums[i] + nums[j]

            freq[nums[i]] -= 1
            if freq[nums[i]] == 0:
                del freq[nums[i]]

            freq[nums[j]] = freq.get(nums[j], 0) + 1

            i += 1
            j += 1

            if len(freq) == k:
                mx = max(mx, cur)

        return mx