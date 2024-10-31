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

            // std::cout<<"\n\n\n-------------------\n";
            // std::cout<<"Parking centro\n";
            // std::cout<<"Elige una opcion\n"<<
            // "1) Entrada de coche\n2) Salida de coche\n3) Mostrar todo\n4) Salir del programa\n";
            
            // \b se usa para regresar un caracter anterior en la terminal
            // std::cout<<"-------(   )-------\b\b\b\b\b\b\b\b\b\b";
            
            input(opcion);

            // std::cout<<"\n";

            switch(opcion){

                case 1: //entrada
                    
                try{

                    // std::cout<<"Ingresa la matricula: ";
                    input(matricula);

                    // std::cout<<"Ingresa la plaza: ";
                    input(plaza);

                    parking.Entrada(matricula, plaza);

                    // std::cout<<"----Ingreso exitoso----\n";

                    std::cout<<parking.getTotalSpots()<<" Plazas totales\n";
                    std::cout<<parking.getOccupiedSpots()<<"  Plazas ocupadas\n";
                    std::cout<<parking.getFreeSpots()<<"  Plazas disponibles\n";

                    std::cout.flush();
                }catch(ParkingException error){

                    std::cerr<<"--------ERROR--------\n";
                    std::cerr<<error.what()<<"\n";
                    std::cout.flush();
                }
                break;
                
                case 2: //salida
                try{
                    std::cout<<"Ingresa la matricula: \n";
                    std::cout.flush();
                    input(matricula);
                    // std::cin>>matricula;

                    parking.Salida(matricula);
                    std::cout<<"----Matricula " + matricula + " eliminado----\n";

                    std::cout<<parking.getTotalSpots()<<" Plazas totales\n";
                    std::cout<<parking.getOccupiedSpots()<<"  Plazas ocupadas\n";
                    std::cout<<parking.getFreeSpots()<<"  Plazas disponibles\n";

                    std::cout.flush();

                }catch(ParkingException error){

                    std::cerr<<"--------ERROR--------\n";
                    std::cerr<<error.what()<<"\n";

                    std::cout.flush();
                }
                break;
                
                case 3: //mostrar todo

                    // std::cout<<"opc 3"<<std::endl;
                    std::cout<<parking.toString()<<std::endl;
                break;
                
                case 4: //salir del programa
                    
                    endProgram = true;
                break;
            }
        }catch(std::runtime_error error){ //predictable errors

            std::cerr<<"--------ERROR--------\n";
            std::cerr<<error.what()<<"\n";
            
            std::cout.flush();
        }catch(...){ //any kind of not known errors
            
            std::cerr<<"--------ERROR--------\n";
            std::cerr<<"Error desconocido\n";
            
            std::cout.flush();
        }
    }

    return 0;
}