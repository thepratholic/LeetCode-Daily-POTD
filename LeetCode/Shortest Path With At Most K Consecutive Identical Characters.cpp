#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        vector<vector<pair<int, int>>> adj(n);

        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
        }

        const int INF = 1e9;
        vector<vector<int>> dist(n, vector<int>(k + 1, INF));

        dist[0][1] = 0;

        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;

        pq.push({0, 0, 1});

        while (!pq.empty()) {
            auto [cost, node, streak] = pq.top();
            pq.pop();

            if (cost > dist[node][streak]) {
                continue;
            }

            if (node == n - 1) {
                return cost;
            }

            for (auto [nei, wt] : adj[node]) {
                int new_streak;

                if (labels[nei] == labels[node]) {
                    new_streak = streak + 1;
                } else {
                    new_streak = 1;
                }

                if (new_streak > k) {
                    continue;
                }

                int new_cost = cost + wt;

                if (dist[nei][new_streak] > new_cost) {
                    dist[nei][new_streak] = new_cost;
                    pq.push({new_cost, nei, new_streak});
                }
            }
        }
        return -1;
    }
};