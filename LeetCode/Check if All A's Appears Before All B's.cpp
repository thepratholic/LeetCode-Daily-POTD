#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool checkString(string s) {
        int n = s.size();
        int last_a = -1;
        int last_b = -1;

        for (int i = 0; i < n; i++) {
            if (s[i] == 'a') {
                if (last_b != -1) return false;

                last_a = i;
            }
            
            else last_b = i;
        }

        return true;
    }
};