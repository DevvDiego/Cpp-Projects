#include <exception>
#include <string>


class ParkingException : public std::exception {

    private:
    std::string message;

    public:
    explicit ParkingException(std::string message) : message(message) {}

    const char* what() const noexcept override {
        
        return message.c_str();
    }
};