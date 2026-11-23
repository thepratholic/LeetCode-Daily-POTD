#include <bits/stdc++.h>
using namespace std;

class ProductOfNumbers {
public:
    vector<int> pref;
    ProductOfNumbers() {
        pref = {1};
    }
    
    void add(int num) {
        if (num == 0) {
            pref = {1};
        }
        else {
            pref.push_back(pref.back() * num);
        }
    }
    
    int getProduct(int k) {
        if (k >= pref.size()) return 0;
        else return pref.back() / pref[pref.size() - 1 - k];
    }
};

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * ProductOfNumbers* obj = new ProductOfNumbers();
 * obj->add(num);
 * int param_2 = obj->getProduct(k);
 */