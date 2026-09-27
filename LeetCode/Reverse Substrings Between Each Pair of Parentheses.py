class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        cur = []

        for ch in s:
            if ch == '(':
                stack.append(cur)
                cur = []

            elif ch == ')':
                cur.reverse()
                prev = stack.pop()
                prev.extend(cur)
                cur = prev

            else:
                cur.append(ch)

        return "".join(cur)