#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int x = nums[n / 2];

        int ans = 0;

        for (auto &i : nums) {
            ans += (abs(x - i));
        }

        return ans;
    }
};