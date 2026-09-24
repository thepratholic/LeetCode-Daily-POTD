from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for idx, num in enumerate(nums):
            tmp = num
            sm = 0

            while tmp > 0:
                ld = tmp % 10
                sm += ld
                tmp //= 10

            if sm == idx:
                return idx

        return -1