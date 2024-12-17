#include <iostream>

using namespace std;

int main(void){
    int N, R;
    cin >> N >> R;
    for(int i=0; i<N;i++){
        int D, A;
        cin >> D >> A;
        if( (D==1 && (1600 <= R && R <= 2799)) || (D==2 && (1200 <= R && R <= 2399)) ){
            // レーティングを更新
            R += A;
        }
    }
    cout << R << endl;

    return 0;
}
