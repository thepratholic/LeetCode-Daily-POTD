#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string digitSum(string s, int k) {
        while (s.size() > k) {
            string next;
            for (int i = 0; i < s.size(); i += k) {
                int sm = 0;

                for (int j = i; j < i + k and j < s.size(); j++) {
                    sm += s[j] - '0';
                }
                next += to_string(sm);
            }
            s = next;
        }

        return s;
    }
};