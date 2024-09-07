#include "main.hpp"

int main(){
    // read values from command
    int32_t num1, num2;
    printf("Input num1: ");
    scanf("%d", &num1);
    printf("Input num2: ");
    scanf("%d", &num2);

    // calc add
    int32_t ret = CalcAdd(num1, num2);
    //int32_t ret = num1 + num2;

    // display added num
    printf("answer = %d\n", ret);

    return 0;
}
