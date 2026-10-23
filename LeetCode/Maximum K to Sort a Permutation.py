from collections import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0

        ans = ~0

        for i, val in enumerate(nums):
            if val != i:
                ans &= val

        return ans