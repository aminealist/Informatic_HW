#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define openf(file) ifstream in(file)
#define fori(start, end) for(ll i = 0; i < end; ++i)

using namespace std;

int counter(const ll m[], ll n, ll finding_value) {
    ll counter = 0;
    fori (0, n) {
        if (m[i] == finding_value) {
            counter++;
        }
    }
    return counter;
}


int main() {
    ll n, k = 1, main_counter = 0;
    openf("26-j1.txt");
    in >> n;
    ll m[n];
    for (ll i = 0; i < n; ++i) {
        in >> m[i];
    }
    sort(m, m + n);
    while (k != 51) {
        if (k == 50) {
            main_counter += counter(m, n, 50) / 2;
            break;
        } else {
            main_counter += min(counter(m, n, 100 - k), counter(m, n, k));
        }
        k++;
    }
    cout << main_counter;
}