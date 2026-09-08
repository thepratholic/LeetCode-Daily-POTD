class Solution:
    def countCommas(self, n: int) -> int:
        tmp = str(n)

        if len(tmp) < 4:
            return 0

        return n - 999