#include<vector>
#include<string>

class Parking{

    private:
    std::string nombre;
    std::vector<std::string> matriculas;

    public:

                                            //inicializando metodos
    Parking(std::string nombre, int tamaño) : matriculas(tamaño,"") {
        this->nombre = nombre; 

    }

    std::string getNombre(){
        return this->nombre;

    }

    void Entrada(std::string matricula, int plaza){
        
        if( matricula.length() < 4 || matricula == "" ){
            throw "Matricula incorrecta";
        }

        if( !this->matriculas.at(plaza).empty() ){
            throw "Plaza ya ocupada";
        }

        if( itExists(matricula) ){
            throw "Matricula repetida";
        }

    }

    private: 
    bool itExists(std::string item){

        bool foundFlag = false;
        for(const auto &matricula : matriculas){
            if(matricula == item){
                return true;
            }
        }

        return false;

    }

};