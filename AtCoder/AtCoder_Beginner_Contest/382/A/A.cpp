#include <iostream>

int main(void) {
    int N, D;
    std::cin >> N >> D;

    std::string S;
    std::cin >> S;

    int akibako = 0;
    for (int i = 0; i < S.size(); i++) {
        if (S[i] == '.') {
            akibako++;
        }
    }

    int ret = akibako + D;
    std::cout << ret << std::endl;

    return 0;
}
