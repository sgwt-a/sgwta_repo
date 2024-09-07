#ifndef CAR_H
#define CAR_H

// define Car Class
class Car{
    public:
        Car();  // コンストラクタ
        ~Car();  // デストラクタ
        void moveCar();  // 移動メソッド
        void supplyFuel(int fuel);  // 燃料補給メソッド
        int public_member;
    private:
        int fuel_;  // 燃料
        int migration_;  // 移動距離
};

#endif // CAR_H
