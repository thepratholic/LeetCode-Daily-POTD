from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [0] * k
        dp = [0] * k

        for x in nums:
            new_dp = [0] * k

            new_dp[x % k] += 1 # new subarray starting from this index

            # existing subarrays ko extend karenge
            for r in range(k):
                if dp[r]: # means pehle koi subarray tha iss remainder k saath, if yes toh x ko bhi include karo
                    new_rem = (r * x) % k
                    new_dp[new_rem] += dp[r]

            dp = new_dp

            for r in range(k):
                res[r] += dp[r]

        return res