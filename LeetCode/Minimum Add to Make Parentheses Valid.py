class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        ans = 0

        for ch in s:
            if ch == '(':
                stack.append(ch)

            else:
                if not stack:
                    ans += 1

                else:
                    stack.pop()

        if stack:
            ans += len(stack)

        return ans