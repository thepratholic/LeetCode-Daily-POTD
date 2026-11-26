class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False

        alice = True
        to_remove = 10

        while n >= to_remove:
            n -= to_remove
            to_remove -= 1
            alice = not alice

        return not alice