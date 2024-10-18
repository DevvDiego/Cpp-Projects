#include <iostream>
#include "parking.cpp"

int main(){

    Parking parking("ola", 10);
    std::cout<<parking.getNombre()<<std::endl;


    return 0;
}