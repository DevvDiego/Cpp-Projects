#include <iostream>
#include <limits>
#include "parking.cpp"


/**
 * Uses cin to read from ifstream, and checks if there is a failbit or badbit set or not.
*/
template <typename T>
void input(T &variableToWrite){

    std::cin>>variableToWrite;

    if(std::cin.fail()){ //wrong data type recieved
        
        std::cin.clear();
        std::cin.ignore( std::numeric_limits<std::streamsize>::max(), '\n'); //ignore the full stream buff
        throw std::runtime_error("Error de tipo de dato");
    }
}


int main(){
    //TODO Make the parking size to act to the user as a 1-10 not 0-10
    // ? is it achievable?

    int opcion;
    int endProgram = false;
    std::string matricula;
    int plaza;



    Parking parking("Parking Centro", 10);

    while( !endProgram ){

        try{

            std::cout<<"\n\n\n-------------------\n";
            std::cout<<"Parking centro\n";
            std::cout<<"Elige una opcion\n"<<
            "1) Entrada de coche\n2) Salida de coche\n3) Mostrar todo\n4) Salir del programa\n";
            
            // \b se usa para regresar un caracter anterior en la terminal
            std::cout<<"-------(   )-------\b\b\b\b\b\b\b\b\b\b";
            input(opcion);
            std::cout<<"\n";

            switch(opcion){

                case 1: //entrada
                    
                try{

                    std::cout<<"Ingresa la matricula: ";
                    input(matricula);
                    // std::cin>>matricula;

                    std::cout<<"Ingresa la plaza: ";
                    input(plaza);
                    // std::cin>>plaza;

                    parking.Entrada(matricula, plaza);

                    std::cout<<"\n----Ingreso exitoso----\n\n";

                    std::cout<<parking.getTotalSpots()<<" Plazas totales\n";
                    std::cout<<parking.getOccupiedSpots()<<" Plazas ocupadas\n";
                    std::cout<<parking.getFreeSpots()<<" Plazas disponibles"<<std::endl;
                }catch(ParkingException error){

                    std::cerr<<"--------ERROR--------\n";
                    std::cerr<<error.what();
                }
                break;
                
                case 2: //salida
                try{
                    std::cout<<"Ingresa la matricula: ";
                    input(matricula);
                    // std::cin>>matricula;

                    parking.Salida(matricula);
                    std::cout<<"\n----Matricula " + matricula + " eliminado----\n\n";

                    std::cout<<parking.getTotalSpots()<<" Plazas totales\n";
                    std::cout<<parking.getOccupiedSpots()<<"  Plazas ocupadas\n";
                    std::cout<<parking.getFreeSpots()<<"  Plazas disponibles"<<std::endl;
                }catch(ParkingException error){

                    std::cerr<<"--------ERROR--------\n";
                    std::cerr<<error.what();
                }
                break;
                
                case 3: //mostrar todo

                    std::cout<<parking.toString();
                break;
                
                case 4: //salir del programa
                    
                    endProgram = true;
                break;
            }
        }catch(std::runtime_error error){ //predictable errors

            std::cerr<<"--------ERROR--------\n";
            std::cerr<<error.what();
        }catch(...){ //any kind of not known errors
        
            std::cerr<<"--------ERROR--------\n";
            std::cerr<<"Error desconocido";
        }
    }






    // parking.Entrada("000-MEX", 0);
    // parking.Entrada("123-MEX", 1);
    // parking.Entrada("321-MEX", 2);
    // parking.Entrada("456-MEX", 3);
    // parking.Entrada("654-MEX", 4);
    // parking.Entrada("789-MEX", 5);
    // parking.Entrada("987-MEX", 6);
    // parking.Entrada("136-MEX", 7);
    // parking.Entrada("631-MEX", 8);
    // parking.Entrada("247-MEX", 9);
    // parking.Entrada("742-MEX", 10);

    return 0;
}