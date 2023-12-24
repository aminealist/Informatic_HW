#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define openf(file) ifstream in(file)
using namespace std;

int main() {
    openf("26-k3.txt");
    ll N, K, M;
    in >> N >> K >> M;
    ll uch[N];
    for (int i = 0; i < N; ++i) {
        in >> uch[i];
    }
    sort(uch, uch + N);
    cout << uch[N -K] << " " << uch[N - (M + K )];
}