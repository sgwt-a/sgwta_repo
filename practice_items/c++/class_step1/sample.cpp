#include "sample.h"

void Sample::set_private_num(int num){
    private_num = num;
}

int Sample::get_private_num(){
    return private_num;
}

int Sample::add_private_public(){
    return private_num + public_num;
}

int Sample::add_private_public_external(int external_num){
    return private_num + public_num + external_num;
}
