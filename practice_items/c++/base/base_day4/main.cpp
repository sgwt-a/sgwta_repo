#include <iostream>
#include "car.h"

int main(){
    // 自動でコンストラクタ/デストラクタが実行される場合
    {
    Car car;  // コンストラクタ実行

    car.supplyFuel(2);

    car.moveCar();
    car.moveCar();
    car.moveCar();

    car.supplyFuel(10);

    car.moveCar();
    car.moveCar();
    car.moveCar();
    car.moveCar();
    car.moveCar();

    //std::cout << car.public_member << std::endl;
    }
    std::cout << "Close scope" << std::endl;
    //car.moveCar();  // スコープ外なのでエラーとなる。

    return 0;  // デストラクタ実行

    // 意図的にコンストラクタ/デストラクタの実行を制御したい場合
    // 例：膨大な画像データを読み込むなど
    
    //Car* pCar = NULL;
    //std::cout << "Car* pCar = NULL を実行しました。" << std::endl;
    //pCar = new Car();  // コンストラクタ実行
    //std::cout << "pCar = new Car() を実行しました。" << std::endl;
    //Car* pCar2 = new Car();
    //std::cout << "Car* pCar2 = new Car() を実行しました。" << std::endl;
    //pCar->supplyFuel(2);
    //pCar->moveCar();
    //pCar->moveCar();
    //pCar->moveCar();
    //pCar->supplyFuel(10);
    //pCar->moveCar();
    //pCar->moveCar();
    //pCar->moveCar();
    //delete pCar;  // デストラクタ実行
    //std::cout << "delete pCar を実行しました。" << std::endl;
    //return 0;
}