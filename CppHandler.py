import subprocess


class CppHandler:
    
    def __init__(self):
        self.process = subprocess.Popen(
            ['./app.exe'],  # List containing the path to the C++ executable
            stdin=subprocess.PIPE,  # Connect the subprocess's standard input (stdin) to a pipe
            stdout=subprocess.PIPE,  # Connect the subprocess's standard output (stdout) to a pipe
            stderr=subprocess.PIPE,
            text=True  # Treat the stdin/stdout as text streams (instead of binary)
        )
        
    def send(self, msg):
        # Send the user input to the C++ program's stdin
        self.process.stdin.write( str(msg) + "\n" )  # "\n marks end of write"
        self.process.stdin.flush()  # Flush the stream to ensure the input is sent immediately

    def read(self):
        output = self.process.stdout.readline().strip()
        
        return output.split(',');


    def insertar(self, plate, spot):
        pass


    def salida(self):
        pass

    def mostrar(self):
        pass



cpp = CppHandler()


i=0;
while True:
    print("\n\n")

    cpp.insertar(plate=input("Plate: "), spot=input("Spot: "))    

    input("EXIT")

