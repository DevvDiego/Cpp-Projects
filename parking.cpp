#include <vector>
#include <string>

class Parking{

    private:
    std::string name;
    std::vector<std::string> plates;

    public:

                                            //inicializando metodos
    Parking(std::string name, int tamaño) : plates(tamaño,"") {
        this->name = name; 

    }

    std::string getNombre(){
        return this->name;

    }

    void Entrada(std::string plate, int plaza){
        
        if( plate.length() < 4 || plate == "" ){
            throw "plate incorrecta";
        }

        if( !this->plates.at(plaza).empty() ){
            throw "Plaza ya ocupada";
        }

        if( itExists(plate) ){
            throw "Matricula repetida";
        }

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