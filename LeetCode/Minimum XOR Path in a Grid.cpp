#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<vector<int>>> dp(m, vector<vector<int>> (n, vector<int> (1024, -1)));

        function<int(int, int, int)> f = [&](int i, int j, int xr) -> int {
            if (i == m - 1 and j == n - 1) {
                return xr ^ grid[i][j];
            }

            if (dp[i][j][xr] != -1) return dp[i][j][xr];

            int ans = INT_MAX;
            int x = grid[i][j] ^ xr;

            if (i + 1 < m) {
                ans = min(ans, f(i + 1, j, x));
            }

            if (j + 1 < n) {
                ans = min(ans, f(i, j + 1, x));
            }

            return dp[i][j][xr] = ans;
        };

        return f(0, 0, 0);
    }
};