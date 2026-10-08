class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        count = 0

        for ch in s:
            if ch == "(":
                count += 1

                if count == 1:
                    pass

                else:
                    stack.append(ch)

            else:
                count -= 1

                if count == 0:
                    pass

                else:
                    stack.append(ch)

        return "".join(stack)