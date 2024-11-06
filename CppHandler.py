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
        

    def send(self, msg:str)->None:
        
        self.process.stdin.write(str(msg) + '\n')
        self.process.stdin.flush()
    

    def stdout_read(self):
        """
        Read from STDOUT of the subprocess
        """
        return self.process.stdout.readline().strip()

    
    def stderr_read(self):
        """
        Read from STDERR of the subprocess
        """
        return self.process.stderr.readline().strip()


    def insertar(self, data:str):
        self.send(1) #option

        self.send(data) #comma separated data

        error = self.stderr_read()
        if(error == "error"):
            print("error")
            print(self.stderr_read())
            
        elif(error == "NONE"):
            print("no errors")
            print(self.stdout_read())


    def salida(self, data:str):
        self.send(2)

        self.send(data)

        error = self.stderr_read()
        if(error == "error"):
            print("error")
            print(self.stderr_read())
            
        elif(error == "NONE"):
            print("no errors")
            print(self.stdout_read())


    def mostrar(self):
        self.send(3)

        print(self.stdout_read())



cpp = CppHandler()


while True:
    opt = int(input("\nopt: "))

    if(opt == 1):
        cpp.insertar(input("comma separated str: "))
    
    elif(opt == 2):
        cpp.salida(input("plate: "))

    elif(opt == 3):
        cpp.mostrar()
    