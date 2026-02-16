class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:].zfill(32)
        
        ans = 0
        for i in range(len(bits)):
            if bits[i] == '1':
                ans |= (1 << i)

        return ans