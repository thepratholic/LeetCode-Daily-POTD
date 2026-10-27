class Solution {
public:
    vector<string> createGrid(int m, int n) {
        vector<vector<char>> ans(m, vector<char>(n, '#'));

        for (int j = 0; j < n; j++) {
            ans[0][j] = '.';
        }

        for (int i = 0; i < m; i++) {
            ans[i][n - 1] = '.';
        }

        vector<string> grid;

        for (int i = 0; i < m; i++) {
            string cur = "";
            for (int j = 0; j < n; j++) {
                cur.push_back(ans[i][j]);
            }

            grid.push_back(cur);
        }

        return grid;
    }
};