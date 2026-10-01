class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        open = {'(', '[', '{'}

        stack = []

        for ch in s:
            if ch in open:
                stack.append(ch)

            else:
                if not stack: return False
                
                if (ch == ')' and stack[-1] == '(') or (ch == ']' and stack[-1] == '[') or (ch == '}' and stack[-1] == '{'):
                    stack.pop()

                else:
                    return False

        return not stack