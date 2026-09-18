class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')

            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            if last[c] == -1:
                continue

            l = first[c]
            r = last[c]

            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x]) # iss current char 'c' ki saari positions cover ho jaye vaha tak hum extend kar rahe hai iss interval ko

                i += 1

            if valid:
                intervals.append((l, r))

        ans = []
        prev = -1

        intervals.sort(key = lambda x : x[1])

        for l, r in intervals:
            if l > prev:
                ans.append(s[l:r + 1])
                prev = r

        return ans