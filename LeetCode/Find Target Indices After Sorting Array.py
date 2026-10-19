class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        ans = []

        for i, val in enumerate(nums):
            if val == target:
                ans.append(i)

        return ans