#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();

        vector<vector<int>> g(n);

        for (int node = 1; node < n; node++) {
            g[parent[node]].push_back(node);
        }

        vector<int> last(26, -1);
        vector<int> new_parent = parent;

        function<void(int)> dfs = [&](int node) {
            int idx = s[node] - 'a';

            if (last[idx] != -1) {
                new_parent[node] = last[idx];
            }

            int old = last[idx];
            last[idx] = node;

            for (int child : g[node]) {
                dfs(child);
            }

            last[idx] = old;
        };

        dfs(0);

        vector<int> ans(n, 0);
        vector<vector<int>> tree(n);

        for (int node = 1; node < n; node++) {
            tree[new_parent[node]].push_back(node);
        }

        function<void(int)> dfs2 = [&](int node) {
            ans[node] = 1;

            for (int child : tree[node]) {
                dfs2(child);
                ans[node] += ans[child];
            }
        };

        dfs2(0);

        return ans;
    }
};