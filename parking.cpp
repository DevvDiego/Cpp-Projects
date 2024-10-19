
























#include <vector>
#include <string>
#include <iostream>

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
        try
        {
            // "" is like a NULL but for std::strings
            if( plate.length() < 4 || plate == "" ){

                throw "Matricula incorrecta";
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
                    this->plates.resize(this->plates.size() + 1, "");
                }
            }

            if( !this->plates.at(spot).empty() ){

                throw "Plaza ya ocupada";
            }

            if( itExists(plate) ){

                throw "Matricula repetida";
            }

            this->plates[spot] = plate;
            occupiedSpots++;
        }catch(const char* e){

            std::cerr << e << '\n';
        }
        
    }

    int Salida(std::string plate){
        
        try{

            //result is the index that the element was found in
            int result = linearSearch(plate, 2);
            
            if( result == -1 ){

                throw "Matricula no existente";
            }

            //set spot with a null plate
            plates[result] = ""; //"" means Null for a string
            occupiedSpots--;

            //returns the index where it was found
            return result;
        }catch(char const* e){

            std::cout<<e<<"\n\n";
        }

        return 1;
    }

    std::string getNombre(){

        return this->name;
    }

    std::string toString(){
        
        std::string output;
        output = output + "\nParking " + this->name + "\n";
        output = output + "---------------\n";
        
        for (int i = 0; i<plates.size(); i++){

            output = output + "Plaza " + std::to_string(i) + ": " + getSpotPlate(i) + "\n";
        }

        return output;
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

    // std::string getSpotPlate(int spot){
        
    //     return plates[spot];
    // }


    private:
    bool itExists(std::string item){

        if( linearSearch(item) != -1 ){

            return true;
        }

        return false;
    }

    std::string getSpotPlate(int spot){

        if( plates[spot] == "" ){

            return "(vacio)";
        }

        return plates[spot];
    }

    int linearSearch(const std::string& target, int mode = 1){

        for(int i; i < plates.size(); i++){

            if(plates[i] == target){
                
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