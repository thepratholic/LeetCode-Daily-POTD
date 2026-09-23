class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target = sum(nums) - x

        if target < 0:
            return -1

        if target == 0:
            return n

        l = 0
        best = -1
        cur = 0

        for r in range(n):
            cur += nums[r]

            while l <= r and cur > target:
                cur -= nums[l]
                l += 1

            if cur == target:
                best = max(best, r - l + 1)

        if best == -1:
            return -1

        return n - best