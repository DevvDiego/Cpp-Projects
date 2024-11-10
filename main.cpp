#include <iostream>
#include <limits>
#include <vector>
#include "parking.cpp"


std::vector<std::string> split(std::string& str, const std::string& delimiter) {
    
    size_t pos = 0;
    std::vector<std::string> tokens;
    std::string token;

    while ( (pos = str.find(delimiter)) != std::string::npos) {
    
        token = str.substr(0, pos);
        tokens.push_back(token);

        str.erase(0, pos + delimiter.length());
    }

    tokens.push_back(str);

    return tokens;
}


std::vector<std::string> parse(std::string msg){

    return split(msg, ",");
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


void cout_send(std::string msg){
    /**
     * !IMPORTANT NOTE
     * Using a newline escape to mark the end of the data sent
     * 
     * python wont parse correctly without it
     * (wont find and end, and might appear no message was sent)
     */
    std::cout<<msg + "\n";
    std::cout.flush();
}

void cerr_send(std::string msg){
    /**
     * !IMPORTANT NOTE
     * Using a newline escape to mark the end of the data sent
     * 
     * python wont parse correctly without it
     * (wont find and end, and might appear no message was sent)
     */
    std::cerr<<msg + "\n";
    std::cerr.flush();

}


int main(){
    //TODO Make the parking size to act to the user as a 1-10 not 0-10
    // ? is it achievable?

    int opcion;
    int endProgram = false;
    
    std::string data;
    std::vector<std::string> data_vec;


    Parking parking("Parking Centro", 10);

    std::string messageToSend;

    while( !endProgram ){

        try{

            input(opcion); //hard coded options, no errors.

            switch(opcion){

                case 1: //entrada
                    
                try{
                    
                    input(data);
                    data_vec = parse(data);
                    
                    parking.Entrada(
                        data_vec.at(0),
                        std::stoi(data_vec.at(1))
                    );

                    cout_send(parking.getFullData());
                    cerr_send("success");

                }catch(ParkingException error){
                    
                    cerr_send("error");
                    cerr_send(error.what());
                }
                break;
                
                case 2: //salida
                try{

                    input(data);
                    data_vec = parse(data);
                    
                    parking.Salida(
                        data_vec.at(0)
                    );

                    cout_send(parking.getFullData());
                    cerr_send("success");
 
                }catch(ParkingException error){
                    cerr_send("error");
                    cerr_send(error.what());
                
                }
                break;
                
                case 3: //mostrar todo
                    try{
                        cout_send( parking.toString() );
                        cerr_send("success");
                    
                    }catch(ParkingException error){
                        cerr_send("error");
                        cerr_send(error.what());
                    }
                    
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