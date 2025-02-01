#include <iostream>
#include <vector>

int main(void) {
    int N, M;
    std::cin >> N >> M;

    std::vector<int> A(N);  // 美食度
    std::vector<int> B(M);  // お寿司の美味しさ
    for (int i = 0; i < N; i++) {
        std::cin >> A[i];
    }
    for (int i = 0; i < M; i++) {
        std::cin >> B[i];
    }


    for (int j = 0; j < M; j++) {  // osushi_M
        int eaten = false;
        for (int i = 0; i < N; i++) {  // hito_N
            if (A[i] <= B[j]) {
                std::cout << i+1 << std::endl;
                eaten = true;
                break;
            }
        }
        if (eaten == false) {
            std::cout << -1 << std::endl;
        }
    }
    
    return 0;
}
