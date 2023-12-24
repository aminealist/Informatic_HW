#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define openf(file) ifstream in(file)
#define fori(start, end) for(ll i = start; i < end; ++i)
using namespace std;


int main() {
    openf("26-k6.txt");
    ll n, k200 = 0;
    in >> n;
    ll a[n];
    fori(0, n) {
        in >> a[i];
        if (a[i] > 200) {
            k200++;
        }
    }
    sort(a, a + n);

}