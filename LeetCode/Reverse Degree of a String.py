class Solution:
    def reverseDegree(self, s: str) -> int:

        ans = 0

        for i, ch in enumerate(s):
            rev_idx = 26 - (ord(ch) - ord('a'))
            ans += rev_idx * (i + 1)

        return ans