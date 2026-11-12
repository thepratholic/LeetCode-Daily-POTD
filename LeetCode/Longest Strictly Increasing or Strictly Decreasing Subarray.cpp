#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int maxi = 1;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int curr = 1;

            for (int j = i + 1; j < n; j++) {
                if (nums[j] > nums[j - 1]) {
                    curr++;
                } else {
                    break;
                }
            }

            maxi = max(maxi, curr);
        }

        for (int i = 0; i < n; i++) {
            int curr = 1;

            for (int j = i + 1; j < n; j++) {
                if (nums[j] < nums[j - 1]) {
                    curr++;
                } else {
                    break;
                }
            }

            maxi = max(maxi, curr);
        }

        return maxi;
    }
};