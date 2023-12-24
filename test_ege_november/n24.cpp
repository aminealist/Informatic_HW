#pragma GCC optimize("Ofast,unroll-loops")

#include <bits/stdc++.h>

#define ll long long
#define ld long double

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    ll left = 0, right = 11, sum = 0, len, counter = 0;
    string input;
    ifstream in;
    ofstream out;


    in.open("24.txt");
    in >> input;
    len = 1100000;
    vector<ll> m(1100000, 0);
    for (int i = 0; i < len; ++i) {
        if (input[i] == 'E') {
            m[i] = 1;
        } else if (input[i] == 'F') {
            m[i] = 9;
        } else {
            m[i] = 0;
        }
    }


    while (true) {
        if (sum == 2) {
            if (m[left] == 1 and m[right] == 1) {
                counter++;
                if (right - left > 11) {
                    sum -= m[left];
                    left++;
                } else {
                    if ()
                }
            }
        }
    }
}