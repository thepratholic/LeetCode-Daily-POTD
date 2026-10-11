#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int sumOfSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> special;

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                special.push_back(nums[i - 1]);
            }
        }

        int ans = 0;
        for (auto &x : special) {
            ans += (x * x);
        }

        return ans;
    }
};