#include <bits/stdc++.h>
using namespace std;

class Solution {
public:

    bool isValid(int i, int j, int m, int n) {
        return i >= 0 and i < m and j >= 0 and j < n;
    } 

    int bfs(int row, int col, vector<vector<bool>> &vis, vector<vector<int>> &grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        vis[row][col] = true;
        queue<pair<int, int>> q;
        q.push({row, col});

        long long sum = grid[row][col];

        vector<pair<int, int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();

            for (auto [dx, dy] : dirs) {
                int nx = dx + x, ny = dy + y;

                if (isValid(nx, ny, m, n) and !vis[nx][ny] and grid[nx][ny] > 0) {
                    vis[nx][ny] = true;
                    q.push({nx, ny});
                    sum += grid[nx][ny];
                }
            }
        }

        return sum % k == 0 ? 1 : 0;
    }
    
    int countIslands(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        int ans = 0;
        vector<vector<bool>> vis(m, vector<bool>(n, false));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (!vis[i][j] && grid[i][j] > 0) {
                    ans += bfs(i, j, vis, grid, k);
                }
            }
        }

        return ans;
    }
};