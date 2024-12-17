#include <iostream>
#include <bitset>
#include <vector>
#include <map>
#include <utility>
#include <algorithm>

// using namespace std;

// 比較関数
bool compare(const std::pair<int, std::string>& a, const std::pair<int, std::string>& b) {  // 引数は&をつけて参照渡しにすると無駄なコピーが削減できてメモリの節約になる。
    if (a.first == b.first) {
        return a.second < b.second; // 得点が同じなら名前を辞書順
    }
    return a.first > b.first; // 得点が高い順
}

int main(void) {
    // 入力の取得
    //int a, b, c, d, e;
    //std::cin >> a >> b >> c >> d >> e;
    //std::vector<int> point = {a, b, c, d, e};
    std::vector<int> point(5);
    for (int i = 0; i < point.size(); i++) {
        std::cin >> point[i];
    }
    // 各参加者の得点の整理
    //std::map<std::string, int> score_list;
    std::vector<std::pair<int, std::string>> score_list;
    //std::string ABCDE = "ABCDE";

    for (int i=1; i <= 31; i++) {
        // i = 1; E
        int score = 0;
        std::string name = "";

        for (int bit = 0; bit < 5; bit++) {
            //std::cout << "i = " << i << "(" << std::bitset<5>(i) << "), bit = " << bit << ", i >> bit = " << (i >> bit) << ", (i >> bit) & 0b00001 = " << ((i >> bit) & 0b00001) << std::endl;
            //if ( (i >> bit) & 0b00001 ) {  // i のbit番目のビットが1の場合
            if ( i & (1 << bit) ) {
                score += point[bit];
                //name += ABCDE[bit];
                name += "ABCDE"[bit];
            }
        }

        //std::pair<int, std::string> score_element(score, name);
        //score_list.push_back(score_element);  // pushバックはvectorの要素の型のオブジェクトを作ってからしか追加できない
        score_list.emplace_back(score, name);
    }

    // 順番に並べ替える
    std::sort(score_list.begin(), score_list.end(), compare);

    // debug
    for (const auto& pair : score_list) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    return 0;
}
