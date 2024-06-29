#include <iostream>
#include "sample.h"

using namespace std;

int main(){
    Sample obj;
    int num = 10;

    // classのpublic変数へのアクセスは容易
    obj.public_num = 100;

    // classのprivate変数へのアクセスはメソッドを介さないと無理っぽい
    obj.set_private_num(num);

    // classのメソッドをコールして結果を表示
    cout << obj.get_private_num() << endl;
    cout << obj.add_private_public() << endl;
    cout << obj.add_private_public_external(33) << endl;

    return 0;
}
