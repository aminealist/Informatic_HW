#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define openf(file) ifstream in(file)
#define fori(start, end) for(ll i = start; i < end; ++i)

using namespace std;


int main() {
    ll n, sum = 0, counter = 0, max_el = 0;
    ld k, inp1, inp2;
    map<ld, vector<ll>> mpk;
    openf("26-k6.txt");
    in >> n >> k;
    cout << n << ' ' << k << "\n";
    fori(0, n) {
        in >> inp1 >> inp2;
        mpk[inp2 / inp1].push_back(inp1);

    }
    for (auto &[key, value]: mpk) {
        sort(mpk[key].begin(), mpk[key].end());
    }
    for (auto &[key, value]: mpk) {
        cout << key << ": ";
        for (ll el: value) {
            if (counter + 1 < k) {
                sum += el;
                max_el = el * key;
                counter++;
            }
            cout << el << ' ';
        }
        cout << "\n";
//        if (coun <= k) {
//            sum += value;
//            maxin = key;
//        }
    }
    cout << sum <<' ' << max_el;
}