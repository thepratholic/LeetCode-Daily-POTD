class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        mx_balance = m + n

        dp = [[[None] * (mx_balance + 1) for _ in range(n)] for _ in range(m)]

        def f(i, j, balance):
            if balance < 0:
                return False

            if i == m - 1 and j == n - 1:
                dp[i][j][balance] = (balance == 0)
                return balance == 0

            if dp[i][j][balance] is not None:
                return dp[i][j][balance]

            res = False
            if i + 1 < m:
                nb = balance + 1 if grid[i + 1][j] == '(' else balance - 1
                res = f(i + 1, j, nb)

            if not res and j + 1 < n:
                nb = balance + 1 if grid[i][j + 1] == '(' else balance - 1
                res = f(i, j + 1, nb)

            dp[i][j][balance] = res
            return res

        return f(0, 0, 1)