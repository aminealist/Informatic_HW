#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define openf(file) ifstream in(file)
using namespace std;

int main() {
    openf("17-243.txt");
    ll a, m_127 = -1, fst, min_s = 111111111111111, k = 0, court = -1;
    vector<ll> chiselki;
    vector<bool> oct_31;
    while (in >> a) {
        court++;
        chiselki.push_back(a);
        oct_31.push_back(false);
        if (a % 127 == 0) {
            if (a > m_127) {
                m_127 = a;
            }
        }
        fst = a % 8;
        a = a / 8;
        while (a > 0) {
            if (fst == 1 and a % 8 == 3) {
                oct_31[court] = true;
                break;
            }
            fst = a % 8;
            a = a / 8;
        }
    }
    for (ll i = 0; i < court + 1; ++i) {
        if ((chiselki[i] > m_127 or chiselki[i - 1] > m_127) and (oct_31[i] == true or oct_31[i - 1] == true)) {
            if ((chiselki[i] + chiselki[i - 1]) < min_s) {
                min_s = chiselki[i] + chiselki[i - 1];
            }
            k++;
        }

    }
    cout << min_s << " " << k;

}