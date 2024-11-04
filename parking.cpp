#include <vector>
#include <string>
#include <iostream>
#include "ParkingException.cpp"

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
        output += this->name + ","; 
        output += "---------------,"; 
        
        for (int i = 0; i < plates.size(); i++){
            //using comma separated values to let python be able to easily separate them.
            output += "Plaza " + std::to_string(i) + ": " + getSpotPlate(i) + ",";
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

    std::string getFullData(){
        
        return std::to_string(this->getTotalSpots())+" Plazas totales\n"+
        std::to_string(this->getOccupiedSpots())+"  Plazas ocupadas\n"+
        std::to_string(this->getFreeSpots())+"  Plazas disponibles\n";
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

        for(int i = 0; i < plates.size(); i++){

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
