from itertools import permutations
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        st = set()

        for perm in permutations(digits, 3):
            if perm[0] == 0 or perm[2] & 1:
                continue

            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            st.add(num)

        return len(st)