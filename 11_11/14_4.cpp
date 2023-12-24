#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define readf(file) ifstream in(file)
#define writef(file) ifstream out(file)
using namespace std;

int main() {
    readf("17-4.txt");
    ll a, min_s=111111111111, k = 0;
    string sa;
    ld sr_zn, s = 0, counter = 0;
    vector<ll> ch;
    vector<unordered_set<ll>> st;
    while (in >> a) {
        s += a;
        counter++;
        ch.push_back(a);
        st.push_back({});
        while (a != 0) {
            st[counter - 1].insert(a % 10);
            a = a / 10;
        }

    }
    sr_zn = s / counter;
    for (ll i = 1; i < counter; ++i) {
        if ((ch[i] < sr_zn or ch[i - 1] < sr_zn) and (st[i].count(5) == 0 or st[i - 1].count(5) == 0)) {
            if ((ch[i] + ch[i - 1]) < min_s) {
                min_s = ch[i] + ch[i - 1];
            }
            k++;
        }
    }
    cout << k << " " << min_s;
}