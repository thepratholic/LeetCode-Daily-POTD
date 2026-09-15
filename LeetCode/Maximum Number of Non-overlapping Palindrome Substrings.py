from functools import cache

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        def check(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False

                i += 1
                j -= 1

            return True

        @cache
        def f(idx):
            if idx >= n:
                return 0

            ans = f(idx + 1)

            for j in range(idx + k - 1, n):
                if check(idx, j):
                    ans = max(ans, 1 + f(j + 1))
                    break

            return ans

        return f(0)