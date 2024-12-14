#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int calcDistance(const vector<int>& a, const vector<int>& b);

int main(void) {
    int H, W, D;
    cin >> H >> W >> D;
    vector<string> S(H);
    for (int i = 0; i < H; i++) {
        cin >> S[i];
        //cout << S[i] << endl;
    }

    int ret = 0;
    for (int i1 = 0; i1 < H; i1++) {
        for (int j1 = 0; j1 < W; j1++) {
            // １つ目の加湿器の場所が決定
            if (S[i1][j1] == '#') continue;
            for (int i2 = 0; i2 < H; i2++) {
                for (int j2 = 0; j2 < W; j2++) {
                    // ２つ目の加湿器の場所が決定
                    if (S[i2][j2] == '#') continue;
                    // 全ての床に対して距離が条件を満たすか確認
                    int count = 0;
                    for (int i = 0; i < H; i++) {
                        for (int j = 0; j < W; j++) {
                            if (S[i][j] == '.' && (abs(i - i1) + abs(j - j1) <= D ||  abs(i - i2) + abs(j - j2) <= D)) {
                                count++;
                            }
                        }
                    }
                    ret = max(ret, count);
                }
            }
        }
    }

    cout << ret << endl;

    return 0;
}

int calcDistance(const vector<int>& a, const vector<int>& b) {
    if (a.size() != 2 || b.size() != 2) {
        throw invalid_argument("Both points must be two-dimensional vectors.");
    }
    return abs(a[0] - b[0]) + abs(a[1] - b[1]);
}
