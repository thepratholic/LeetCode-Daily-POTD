class Solution:
    def binaryGap(self, n: int) -> int:
        bits = bin(n)[2:]
        prev = -1
        ans = 0

        for i, b in enumerate(bits):
            if b == '1':
                if prev != -1:
                    ans = max(ans, i - prev)

                prev = i

        return ans