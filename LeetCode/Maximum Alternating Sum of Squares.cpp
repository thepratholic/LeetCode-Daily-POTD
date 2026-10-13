#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n; i++)
            nums[i] = abs(nums[i]);

        sort(nums.begin(), nums.end());

        deque<int> q(nums.begin(), nums.end());

        long long ans = 0;
        bool pos = true;

        while (!q.empty()) {
            long long val;

            if (pos) {
                val = q.back();
                q.pop_back();
                ans += val * val;
            } 
            else {
                val = q.front();
                q.pop_front();
                ans -= val * val;
            }

            pos = !pos;
        }

        return ans;
    }
};