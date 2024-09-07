#include <iostream>
#include "rat.h"

// 静的メンバ変数の初期化はソースファイルで行われるのが一般的
int Rat::count_ = 0;
int Rat::countPublic_ = 110;

Rat::Rat() : id_(0) {
    id_ = count_;
    count_++;
}

Rat::~Rat() {
    std::cout << "Rat: id = " << id_ << std::endl;
    count_--;
}

void Rat::showNum(){
    std::cout << "Rat number = " << count_ << std::endl;
}

void Rat::squeak(){
    std::cout << id_ << ": chu~chu~" << std::endl;
}
