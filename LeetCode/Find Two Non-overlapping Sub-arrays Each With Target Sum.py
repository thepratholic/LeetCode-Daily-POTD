class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')

        min_len = [INF] * n
        cur = 0
        ans = INF

        i = 0
        best_len = INF

        for j in range(n):
            cur += arr[j]

            while i < j and cur > target:
                cur -= arr[i]
                i += 1

            if cur == target:
                length = j - i + 1

                if i > 0:
                    ans = min(ans, length + min_len[i - 1])

                best_len = min(best_len, length)

            min_len[j] = best_len

        return -1 if ans == INF else ans