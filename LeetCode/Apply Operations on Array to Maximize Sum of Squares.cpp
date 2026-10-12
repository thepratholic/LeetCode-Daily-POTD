#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSum(vector<int>& nums, int k) {
        int MOD = 1e9 + 7;
        vector<int> count(32, 0);

        for (auto &x : nums) {
            for (int i = 0; i < 32; i++) {
                if (x & (1 << i)) count[i]++;
            }
        }

        long long res = 0;
        while (k--) {
            long long cur = 0;

            for (int bit = 0; bit < 32; bit++) {
                if (count[bit] > 0) {
                    count[bit]--;
                    cur = cur | (1 << bit);
                }
            }

            res += (cur * cur);
            res %= MOD;
        }

        return res;
    }
};