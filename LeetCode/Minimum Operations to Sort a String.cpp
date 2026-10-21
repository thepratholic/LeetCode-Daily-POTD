#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minOperations(string s) {
        int n = s.size();

        if (is_sorted(s.begin(), s.end())) {
            return 0;
        }

        if (n == 2) {
            return -1;
        }

        char mn = *min_element(s.begin(), s.end());
        char mx = *max_element(s.begin(), s.end());

        if (s[0] == mn or s[n - 1] == mx) return 1;

        int cnt_mn = count(s.begin(), s.end(), mn);
        int cnt_mx = count(s.begin(), s.end(), mx);

        if (s[0] == mx and s[n - 1] == mn and cnt_mn == 1 and cnt_mx == 1) {
            return 3;
        }

        return 2;
    }
};