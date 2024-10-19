#include <iostream>
#include "parking.cpp"

int main(){

    Parking parking("ola", 10);
    
    parking.Entrada("123-MEX", 1);
    parking.Entrada("321-MEX", 2);
    parking.Entrada("456-MEX", 3);
    parking.Entrada("654-MEX", 4);
    parking.Entrada("789-MEX", 5);
    parking.Entrada("987-MEX", 6);
    parking.Entrada("136-MEX", 7);
    parking.Entrada("631-MEX", 8);
    parking.Entrada("247-MEX", 9);
    parking.Entrada("742-MEX", 10);

    // CASO: Salida exitosa
    // std::cout<<"Salida de main: "<<parking.Salida("247-MEX")<<std::endl;
    // if(parking.getSpotPlate(9) == ""){
    //     std::cout<<"Valor realmente eliminado"<<std::endl;
    // }

    // CASO: Salida fallida
    // std::cout<<"Salida de main: "<<parking.Salida("247000-MEX")<<std::endl;

    // CASO: Matricula < 4
    // parking.Entrada("12", 20);
    // std::cout<<parking.getMaxSpots()<<std::endl;

    //CASO: Matricula == ""
    // parking.Entrada("", 20);
    // std::cout<<parking.getMaxSpots()<<std::endl;

    return 0;
}