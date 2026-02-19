class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        grps = []
        count = 1

        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1

            else:
                grps.append(count)
                count = 1

        grps.append(count)

        ans = 0
        for i in range(1, len(grps)):
            ans += min(grps[i], grps[i - 1])

        return ans