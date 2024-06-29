#include <iostream>
#include "car.h"

int main(){
    Car car;

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

    return 0;
}