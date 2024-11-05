#include <exception>
#include <string>


class ParkingException : public std::exception {

    private:
    std::string message;

    public:
    explicit ParkingException(const std::string& msg) {
        this->message = msg;
    }

    const char* what() const noexcept override {
        
        return message.c_str();
    }
};