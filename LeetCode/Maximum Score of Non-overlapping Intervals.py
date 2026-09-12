from typing import List
from bisect import bisect_right
from functools import cache

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = [[l, r, w, i] for i, (l, r, w) in enumerate(intervals)]

        arr.sort()

        starts = [x[0] for x in arr]

        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1]) # humein L chahiye jo current R se > ho

        @cache
        def f(i, k):
            if i == n or k == 0:
                return 0, ()

            skip_score, skip_indices = f(i + 1, k)

            take_score, take_indices = f(nxt[i], k - 1)

            take_score += arr[i][2]
            take_indices = tuple(sorted(take_indices + (arr[i][3], )))

            if take_score > skip_score:
                return take_score, take_indices

            if skip_score > take_score:
                return skip_score, skip_indices

            if take_indices < skip_indices:
                return take_score, take_indices

            return skip_score, skip_indices

        return list(f(0, 4))[1]