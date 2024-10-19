#include <vector>
#include <string>

class Parking{

    private:
    std::string name;
    std::vector<std::string> plates;
    size_t totalSpots;

    public:

                                            //inicializando metodos
    Parking(std::string name, int size) : plates(size,"") {
        this->name = name; 
        this->totalSpots = this->plates.capacity();
    }

    void Entrada(std::string plate, int spot){
        
        if( plate.length() < 4 || plate == "" ){

            throw "Matricula incorrecta";
        }

        if( spot >= this->plates.size() ){

            while( spot >= this->plates.size() ){
                /**
                 * Sets the new size of the vector to 
                 * the same size it had, but adds one due to
                 * it checking always that it has >= of the max size
                 * 
                 * (max size plus one)
                 */
                this->plates.resize(this->plates.size() + 1, "");
                
                this->totalSpots = this->plates.size();
            }

        }

        if( !this->plates.at(spot).empty() ){

            throw "Plaza ya ocupada";
        }

        if( itExists(plate) ){

            throw "Matricula repetida";
        }

        this->plates[spot];

    }

    std::string getNombre(){

        return this->name;
    }

    size_t getMaxSpots(){

        return this->totalSpots;
    }


    private: 
    bool itExists(std::string item){

        bool foundFlag = false;
        for(const auto &matricula : plates){
            if(matricula == item){
                return true;
            }
        }

        return false;

    }

};