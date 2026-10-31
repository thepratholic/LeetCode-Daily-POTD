#include <bits/stdc++.h>
using namespace std;

class Solution {
    const int MOD = 1e9 + 7;
    int m, n;
    vector<vector<int>> grid;
    vector<vector<vector<int>>> dp;

    int f(int i, int j, int dir) {
        if (i >= m or j >= n) return 0;
        if (i == m - 1 and j == n - 1) return 1;

        int &ans = dp[i][j][dir];

        if (ans != -1) return dp[i][j][dir];

        if (grid[i][j] == 1) {
            if (dir == 0) {
                ans = f(i + 1, j, 1);
            }

            else {
                ans = f(i, j + 1, 0);
            }
        }

        else {
            ans = (f(i + 1, j, 1) + f(i, j + 1, 0)) % MOD;
        }

        return ans;
    }

public:
    int uniquePaths(vector<vector<int>>& grid) {
        this->grid = grid;
        m = grid.size();
        n = grid[0].size();

        if (m == 1 and n == 1) return 1;

        dp.assign(m, vector<vector<int>> (n, vector<int> (2, -1)));

        return (f(0, 1, 0) + f(1, 0, 1)) % MOD;

    }
};