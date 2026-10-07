from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        best = float('inf')
        ans = set()

        def valid(t):
            bal = 0
            for ch in t:
                if ch == '(':
                    bal += 1

                elif ch == ')':
                    bal -= 1

                    if bal < 0:
                        return False

            return bal == 0


        def f(idx, removed, path):
            nonlocal best

            if removed > best:
                return

            if idx == n:
                cur = "".join(path)
                if valid(cur):

                    if removed < best:
                        best = removed
                        ans.clear()
                        ans.add(cur)

                    elif removed == best:
                        ans.add(cur)

                return

            ch = s[idx]

            if ch != '(' and ch != ')':
                path.append(ch)
                f(idx + 1, removed, path)
                path.pop()
                return

            path.append(ch)
            f(idx + 1, removed, path)
            path.pop()

            f(idx + 1, removed + 1, path)
            return

        f(0, 0, [])
        return list(ans)