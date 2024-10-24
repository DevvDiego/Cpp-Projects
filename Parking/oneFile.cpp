#include <vector>
#include <string>
#include <iostream>
#include <limits>
#include <exception>


class ParkingException : public std::exception {

    private:
    std::string message;

    public:
    explicit ParkingException(const std::string& msg, const std::string& funcName, int lineNumber) {
        this->message = msg + " (in function [" + funcName + "] at line [" + std::to_string(lineNumber) + "])";
    }

    const char* what() const noexcept override {
        
        return message.c_str();
    }
};



class Parking{

    private:
    std::string name;
    std::vector<std::string> plates;
    int occupiedSpots;

    public:

                                          //inicializando metodos
    Parking(std::string name, int size) : plates(size,"") {

        this->name = name;
        this->occupiedSpots = 0;
    }

    void Entrada(std::string plate, int spot){

        // "" is like a NULL but for std::strings
        if( plate.length() < 4 || plate == "" ){

            throw ParkingException("Matricula incorrecta", __func__, __LINE__);
        }

        if( spot >= this->plates.size() ){

            while( spot >= this->plates.size() ){
                
                /*
                * Sets the new size of the vector to 
                * the same size it had, but adds one due to
                * it checking always that it has >= of the max size
                * 
                * (max size plus one)
                */
                this->plates.resize( this->plates.size() + 1, "" );
            }
        }

        if( !this->plates.at(spot).empty() ){

            throw ParkingException("Plaza ya ocupada", __func__, __LINE__);
        }

        if( itExists(plate) ){

            throw ParkingException("Matricula repetida", __func__, __LINE__);
        }

        this->plates.at(spot) = plate;
        occupiedSpots++;
    }

    int Salida(std::string plate){

        //result is the index that the element was found in
        int result = linearSearch(plate, 2);
        
        if( result == -1 ){

            throw ParkingException("Matricula no existente", __func__, __LINE__);
        }

        //set spot with a null plate
        plates.at(result) = ""; //"" means Null for a string
        occupiedSpots--;

        //returns the index where it was found
        return result;
    }

    std::string toString(){
        
        std::string output;
        output = output + "\n" + this->name + "\n";
        output = output + "---------------\n";
        
        for (int i = 0; i<plates.size(); i++){

            output = output + "Plaza " + std::to_string(i) + ": " + getSpotPlate(i) + "\n";
        }

        return output;
    }

    std::string getNombre(){

        return this->name;
    }

    int getTotalSpots(){

        return this->plates.size();
    }

    int getOccupiedSpots(){

        return this->occupiedSpots;
    }

    int getFreeSpots(){

        return this->plates.size() - this->occupiedSpots;
    }

    private:
    bool itExists(std::string item){

        if( linearSearch(item) != -1 ){

            return true;
        }

        return false;
    }

    std::string getSpotPlate(int spot){

        if( plates.at(spot) == "" ){

            return "(vacio)";
        }

        return plates.at(spot);
    }

    int linearSearch(const std::string& target, int mode = 1){

        for(int i; i < plates.size(); i++){

            if(plates.at(i) == target){
                
                switch(mode){
                    case 1:
                        return 1; //it is true that the element exists

                    case 2:
                        return i; //returns the index where it was found
                }
            }
        }

        //using -1 to differentiate a NOT FOUND
        //of a index at 0 found
        return -1; //not found
    }

};


// #include "parking.cpp"


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