class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        lo = hi = 0

        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1

            elif ch == ')':
                lo -= 1
                hi -= 1

            else:
                lo -= 1
                hi += 1

            lo = max(lo, 0)

            if hi < 0:
                return False

        return lo == 0