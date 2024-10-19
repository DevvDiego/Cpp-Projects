#include <vector>
#include <string>
#include <iostream>

class Parking{

    private:
    std::string name;
    std::vector<std::string> plates;

    public:

                                          //inicializando metodos
    Parking(std::string name, int size) : plates(size,"") {
        this->name = name;
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
        }catch(const char* e){

            std::cerr << e << '\n';
        }
        
    }

    std::string getNombre(){

        return this->name;
    }

    std::string getSpotPlate(int spot){
        return plates[spot];
    }

    size_t getMaxSpots(){

        return this->plates.size();
    }


    private:
    bool itExists(std::string item){

        //? place value by reference instead of value
        for(int i = 0; i<plates.size(); i++){

            if(plates[i] == item){
                
                return true;
            }
        }

        return false;
    }

};