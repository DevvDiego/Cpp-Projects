import subprocess

class cppConnector:
    def __init__(self):
        self.process = subprocess.Popen(
            ['./app.exe'],  # List containing the path to the C++ executable
            stdin=subprocess.PIPE,  # Connect the subprocess's standard input (stdin) to a pipe
            stdout=subprocess.PIPE,  # Connect the subprocess's standard output (stdout) to a pipe
            text=True  # Treat the stdin/stdout as text streams (instead of binary)
        )


    def send_cpp(self, msg):
        # Send the user input to the C++ program's stdin
        self.process.stdin.write(str(msg) + "\n")  # "\n marks end of write"
        self.process.stdin.flush()  # Flush the stream to ensure the input is sent immediately

    def read_cpp(self):
        output = self.process.stdout.readline().strip()
        
        return output.split(',');



