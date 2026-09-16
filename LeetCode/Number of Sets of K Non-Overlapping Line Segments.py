class Solution:
    def numberOfSets(self, n: int, K: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (n + 1) for _ in range(K + 1)]

        for i in range(n):
            dp[0][i] = 1

        for k in range(1, K + 1):
            prev = [0] * (n + 1)

            for x in range(n - 1, -1, -1):
                prev[x] = (prev[x + 1] + dp[k - 1][x]) % MOD

            for i in range(n - 1, -1, -1):
                skip = dp[k][i + 1]

                take = prev[i + 1]

                dp[k][i] = (take + skip) % MOD

        return dp[K][0]