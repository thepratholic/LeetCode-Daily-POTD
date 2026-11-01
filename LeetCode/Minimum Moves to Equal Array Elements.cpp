#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        int mn = *min_element(nums.begin(), nums.end());

        int ans = 0;

        for (auto &x : nums) {
            ans += (x - mn);
        }

        return ans;

    }
};