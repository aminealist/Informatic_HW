#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define openf(file) ifstream in(file)
#define fori(start, end) for(ll i = start; i < end; ++i)
using namespace std;

int counters(const ll m[], ll n, ll finding_value) {
    ll cou = 0;
    fori (0, n) {
        if (m[i] == finding_value) {
            cou++;
        }
    }
    return cou;
}

int main() {
    ll n, counter = 0, min_counter = 0, mini = 10000000000;
    openf("26-J5.txt");
    in >> n;
    ll m[n], medians[n];
    ll to_med[3];
    fori (0, n) {
        in >> m[i];

    }
    medians[0] = m[0];
    medians[n - 1] = m[n - 1];
    fori (2, n) {
        to_med[0] = m[i - 2];
        to_med[1] = m[i - 1];
        to_med[2] = m[i];
        sort(to_med, to_med + 3);
        medians[i - 1] = to_med[1];
        if (to_med[1] < mini) {
            mini = to_med[1];
            min_counter = 1;
        } else if (mini == to_med[1]) {
            min_counter++;
        }
    }
    fori(0, n) {
        if (m[i] >= medians[i]) {
            counter += m[i] - medians[i];
        }
    }
    cout << min_counter << ' ' << counter;
}