from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []

        for h in range(12):
            for mins in range(60):
                if bin(h).count("1") + bin(mins).count("1") == turnedOn:
                    
                    time = str(h) + ":" + str(mins).zfill(2)
                    ans.append(time)

        return ans