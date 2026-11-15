#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        const int MOD = 1e9 + 7;
        int even = 1;
        int odd = 0;
        int pref = 0;
        long long ans = 0;

        for (int num : arr) {
            pref = (pref + num) % 2;

            if (pref & 1) {
                ans += even;
                odd++;
            }

            else {
                ans += odd;
                even++;
            }

            ans %= MOD;
        }

        return ans;
    }
};