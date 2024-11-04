#include <iostream>
#include <limits>
#include "parking.cpp"

// Communication status for the pipe with python
enum Status{
    OK = 1,
    READY = 2,

    BAD_CALL = 3,
    BAD_TYPE = 4,
    BAD_ANSWER = 5,
};

std::string statusToString(Status st){

    switch(st){

        case OK: return "OK";
        case READY: return "READY";
        case BAD_CALL: return "BAD_CALL";
        case BAD_TYPE: return "BAD_TYPE";
        case BAD_ANSWER: return "BAD_ANSWER";

        default: return "UNKNOWN";
    }
}

/**
 * Uses cin to read from ifstream, and checks if there is a failbit or badbit set or not.
*/
template <typename T>
void input(T &variableToWrite){

    std::cin>>variableToWrite;

    if(std::cin.fail()){ //wrong data type recieved
        
        std::cin.clear();
        std::cin.ignore( std::numeric_limits<std::streamsize>::max(), '\n' ); //ignore the full stream buff
        throw std::runtime_error("Error de tipo de dato");
    }
}


void send(std::string msg){

    std::cout<<msg + "\n";
    std::cout.flush();
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

            send(statusToString(READY));
            input(opcion);

            switch(opcion){

                case 1: //entrada
                    
                try{
                    
                    // sendStatus();
                    input(matricula);

                    input(plaza);

                    parking.Entrada(matricula, plaza);

                    parking.getFullData();
                    std::cout.flush();
                }catch(ParkingException error){

                    std::cerr<<"ERROR\n";
                    std::cerr<<error.what()<<"\n";
                    std::cout.flush();
                }
                break;
                
                case 2: //salida
                try{
                    // std::cout<<"Ingresa la matricula: \n";
                    // std::cout.flush();
                    input(matricula);

                    parking.Salida(matricula);
                    // std::cout<<"----Matricula " + matricula + " eliminado----\n";

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