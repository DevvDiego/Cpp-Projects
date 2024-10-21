#include <exception>
#include <string>


class ParkingException : public std::exception {

    private:
    std::string message;

    public:
    explicit ParkingException(const std::string& msg, const std::string& funcName, int lineNumber) {
        this->message = msg + " (in function [" + funcName + "] at line [" + std::to_string(lineNumber) + "]";
    }

    const char* what() const noexcept override {
        
        return message.c_str();
    }
};