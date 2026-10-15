#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            set<int> seen;
            for (int j = i; j < n; j++) {
                seen.insert(nums[j]);
                int sz = seen.size();
                ans += (sz * sz);
            }
        }

        return ans;
    }
};