#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int N;
    char c1, c2;
    //string c1, c2;  // string型にする場合は下記のif文でc1 -> c1[0], c2 -> c2[0]のようにする必要がある。
    string S;
    cin >> N >> c1 >> c2 >> S;
    //cin >> S;
    // cout << N << ", " << c1 << ", " << c2 << ", " << S << endl;

    for ( int i = 0; i < S.size(); i++ ) {
        // cout << S[i] << ", " << c1 << endl;
        if ( S[i] != c1) {
            S[i] = c2;
        }
    }

    cout << S << endl;

    return 0;
}
