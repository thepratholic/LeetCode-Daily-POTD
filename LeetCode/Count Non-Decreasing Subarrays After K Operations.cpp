#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        deque<pair<long long, long long>> dq;
        long long cost = 0, ans = 0;
        int r = n - 1;

        for (int l = n - 1; l >= 0; --l) {
            long long v = nums[l], cnt = 1;

            while (!dq.empty() && dq.front().first <= v) {
                cost += (v - dq.front().first) * dq.front().second;
                cnt += dq.front().second;
                dq.pop_front();
            }
            dq.push_front({v, cnt});

            while (cost > k) {
                cost -= dq.back().first - nums[r];
                if (--dq.back().second == 0) dq.pop_back();
                --r;
            }

            ans += r - l + 1;
        }
        return ans;
    }
};