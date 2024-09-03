#include <iostream>
#include "car.h"

// コンストラクタ
Car::Car() : public_member(1), fuel_(0), migration_(0){
    std::cout << "Generate Car object." << std::endl;
    std::cout << "  Initialize member variables..." << std::endl;
    std::cout << "    fuel_ = " << fuel_ << std::endl;
    std::cout << "    migration_ = " << migration_ << std::endl;
}

// デストラクタ
Car::~Car(){
    std::cout << "Delete Car object." << std::endl;
    std::cout << "  Finalize member variables..." << std::endl;
    std::cout << "    fuel_ = " << fuel_ << std::endl;
    std::cout << "    migration_ = " << migration_ << std::endl;
}

// 移動メソッド
void Car::moveCar(){
    if(fuel_ > 0){
        migration_++;
        fuel_--;
        std::cout << "Car Moving!" << std::endl;
        std::cout << "  migration_ : " << migration_ << std::endl;
        std::cout << "  fuel_ : " << fuel_ << std::endl;
    } else {
        std::cout << "Car can not move. Please supply fuel..." << std::endl;
    }
}


// 燃料補給メソッド
void Car::supplyFuel(int fuel){
    if(fuel > 0){
        fuel_ += fuel;
        std::cout << "Fuel supplied!" << std::endl;
        std::cout << "  fuel_ : " << fuel_ << std::endl;
    } else {
        std::cout << "Failed to supply fuel..." << std::endl;
    }
}


