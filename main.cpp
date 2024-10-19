#include <iostream>
#include "parking.cpp"

int main(){

    Parking parking("ola", 10);
    std::cout<<parking.getNombre()<<std::endl;
    std::cout<<parking.getMaxSpots()<<std::endl;



    std::cout<<"\n\n";
    parking.Entrada("123-MXSD", 10);
    std::cout<<parking.getMaxSpots()<<std::endl;

    parking.Entrada("12321312312", 15);
    std::cout<<parking.getMaxSpots()<<std::endl;

    parking.Entrada("12321312312", 20);
    std::cout<<parking.getMaxSpots()<<std::endl;

    return 0;
}