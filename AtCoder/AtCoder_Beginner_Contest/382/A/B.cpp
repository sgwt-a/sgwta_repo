#include <iostream>

int main(void) {
    int N, D;
    std::cin >> N >> D;

    std::string S;
    std::cin >> S;

    int eat = 0;
    for (int i = S.size() - 1; 0 <= i; i--) {
        if (S[i] == '@') {
            S[i] = '.';
            eat++;
            if (eat >= D) {
                break;
            }
        }
    }

    for (int i = 0; i < S.size(); i++) {
        std::cout << S[i];
    }
    std::cout << std::endl;

    return 0;
}
