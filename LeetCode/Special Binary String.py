class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        def f(s):
            cnt = 0
            start = 0
            res = []
            for i in range(len(s)):
                cnt += 1 if s[i] == '1' else -1

                if cnt == 0:
                    inner = s[start + 1 : i]
                    best = f(inner)
                    start = i + 1
                    res.append("1" + best + "0")

            res.sort(reverse = True)

            return "".join(res)

        return f(s)