class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        knowledge = dict(knowledge)

        stack = []

        for i, ch in enumerate(s):
            if ch != ')':
                stack.append(ch)
                continue

            key = ""
            while stack and stack[-1] != '(':
                key += stack.pop()

            stack.pop()

            key = key[::-1]
            stack.append(knowledge.get(key, "?"))

        return "".join(stack)