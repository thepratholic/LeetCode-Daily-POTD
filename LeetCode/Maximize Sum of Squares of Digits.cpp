#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        if (sum > 9 * num) return "";

        string ans = "";

        while (num--) {
            int digit = min(9, sum);
            sum -= digit;
            ans += char('0' + digit);
        }

        if (sum) return "";
        return ans;
    }
};