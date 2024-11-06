import subprocess
import os

def parseInput(str:str):
    str = str.strip().split(",")
    print(str)
    return



class CppHandler:
    
    def __init__(self):
        self.process = subprocess.Popen(
            ['./app.exe'],  # List containing the path to the C++ executable
            stdin=subprocess.PIPE,  # Connect the subprocess's standard input (stdin) to a pipe
            stdout=subprocess.PIPE,  # Connect the subprocess's standard output (stdout) to a pipe
            stderr=subprocess.PIPE,
            text=True  # Treat the stdin/stdout as text streams (instead of binary)
        )
        
    # def send(self, msg):
    #     # Send the user input to the C++ program's stdin
    #     self.process.stdin.write( str(msg) + "\n" )  # "\n marks end of write"
    #     self.process.stdin.flush()  # Flush the stream to ensure the input is sent immediately

    # def read(self):        
    #     return self.process.stdout.readline().strip();

    def send(self, msg:str)->None:
        
        self.process.stdin.write(str(msg) + '\n')
        self.process.stdin.flush()
        return
    
    def stdout_read(self):
        return self.process.stdout.readline().strip()

    def stderr_read(self):
        return self.process.stderr.readline().strip()
        

    def insertar(self, data:str):
        self.send(1)

        self.send(data)

        error = self.stderr_read()
        if(error == "error"):
            print("\nerror en insertar " + self.stderr_read())
            
        elif(error == "NONE"):
            print("no errors")
            print(self.stdout_read())

        # self.send(1) # opt

        # self.send(data)

        # print( self.read() )#OK code #? unnecessary?
        # print( self.read() )

        # ! CHECK USAGE possible solution
        # proc = self.process.stdin.readline().strip()
        # proc.startswith("OK") #? use??

    def salida(self):
        pass

    def mostrar(self):
        self.send(3)

        print(self.stdout_read())
        pass



cpp = CppHandler()


while True:
    opt = int(input("opt: "))

    if(opt == 1):
        cpp.insertar(input("comma separated str: "))
    
    elif(opt == 3):
        cpp.mostrar()
    
    elif(opt == 0):
        os.system("cls")