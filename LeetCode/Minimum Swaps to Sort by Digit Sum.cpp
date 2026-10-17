#include <bits/stdc++.h>
#include <tuple>
using namespace std;

class Solution {
public:
    int get(int x) {
        int sum = 0;
        while (x > 0) {
            int ld = x % 10;
            x /= 10;
            sum += ld;
        }
        return sum;
    }

    int minSwaps(vector<int>& nums) {
        int n = nums.size();
        vector<tuple<int, int, int>> a;

        for (int i = 0; i < n; i++) {
            int digit_sum = get(nums[i]);
            a.push_back({digit_sum, nums[i], i});
        }

        sort(a.begin(), a.end());

        vector<int> vis(n, 0);
        int swaps = 0;

        for (int i = 0; i < n; i++) {
            if (vis[i] or get<2>(a[i]) == i) continue;

            int j = i;
            int cnt = 0;

            while (!vis[j]) {
                vis[j] = 1;
                j = get<2>(a[j]);
                cnt++;
            }

            swaps += (cnt - 1);
        }

        return swaps;
    }
};