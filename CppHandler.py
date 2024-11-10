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
        """
        NOTE keep the data str comma separates like "123,123"
        not like "123, 123"
        """

        self.send(1) #option

        self.send(data) #comma separated data

        # TODO handle errors here and in each page

        # For checking errors, if no errors then
        # we expect to stout to have some data
        # otherwise if we find an error on stderr
        # we dont expect nothing so we dont read stdout

        status = self.stderr_read();
        if(status == "error"):

            return {
                "status":"error",
                "message":self.stderr_read()
                }
            
        elif(status == "success"):
            
            return {
                "status":"success",
                "message":self.stdout_read()
                }            


    def salida(self, data:str):
        self.send(2)

        self.send(data)

        status = self.stderr_read();
        if(status == "error"):

            return {
                "status":"error",
                "message":self.stderr_read()
                }
            
        elif(status == "success"):
            
            return {
                "status":"success",
                "message":self.stdout_read()
                }            


    def mostrar(self):
        self.send(3)
        return self.stdout_read()


    def endProgram(self):
        self.send(4)