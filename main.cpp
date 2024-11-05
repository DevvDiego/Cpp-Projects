#include <iostream>
#include <limits>
#include "parking.cpp"

// Communication status for the pipe with python
enum Status{
    OK,
    READY,
    BAD_CALL,
    BAD_TYPE,
    BAD_ANSWER,
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
    /**
     * !Remember to use "," to repalce the newline character on large texts
     * !or else they will buffer differently when python reads
     */
    std::cout<<msg + "\n";
    std::cout.flush();
}

void err_send(std::string msg){
     /**
     * !Remember to use "," to repalce the newline character on large texts
     * !or else they will buffer differently when python reads
     */
    std::cerr<<msg + "\n";
    std::cerr.flush();   
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

            input(opcion);

            switch(opcion){

                case 1: //entrada
                    
                try{

                    parking.Entrada(matricula, plaza);
                    
                    
                }catch(ParkingException error){

                    std::cerr<<"--------ERROR--------\n";
                    std::cerr<<error.what()<<"\n";

                    std::cerr.flush();
                
                }
                break;
                
                case 2: //salida
                try{

                    input(matricula);

                    parking.Salida(matricula);

                    send( parking.getFullData() );

                }catch(ParkingException error){

                    std::cerr<<"--------ERROR--------\n";
                    std::cerr<<error.what()<<"\n";

                    std::cerr.flush();
                }
                break;
                
                case 3: //mostrar todo
                    
                    parking.toString(); 
                break;
                
                case 4: //salir del programa
                    
                    endProgram = true;
                break;
            }
        }catch(std::runtime_error error){ //predictable errors

            std::cerr<<"--------ERROR--------\n";
            std::cerr<<error.what()<<"\n";

            std::cerr.flush();
        
        }catch(...){ //any kind of not known errors
            
            std::cerr<<"--------ERROR--------\n";
            std::cerr<<"Error desconocido\n";
            
            std::cerr.flush();
        }
    }

    return 0;
}