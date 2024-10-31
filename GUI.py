import subprocess

def send_cpp(msg):
    # Send the user input to the C++ program's stdin
    process.stdin.write(str(msg) + "\n")  # "\n marks end of write"
    process.stdin.flush()  # Flush the stream to ensure the input is sent immediately

def read_cpp():
    output = process.stdout.readline().strip()
    
    return output.split(',');





process = subprocess.Popen(
    ['./app.exe'],  # List containing the path to the C++ executable
    stdin=subprocess.PIPE,  # Connect the subprocess's standard input (stdin) to a pipe
    stdout=subprocess.PIPE,  # Connect the subprocess's standard output (stdout) to a pipe
    text=True  # Treat the stdin/stdout as text streams (instead of binary)
)

while True:
    
    print(
        "Elige una opcion\n"+
        "1) Entrada de coche\n"
        "2) Salida de coche\n"
        "3) Mostrar todo\n"
        "4) Salir del programa\n"
        );

    option = str(input("--(   )--\b\b\b\b\b"));

    if(option == "1"):
        send_cpp(option);

        send_cpp( input("Matricula: ") );

        send_cpp( input("Plaza: ") );

        print( read_cpp() )
        print( read_cpp() )
        print( read_cpp() )

    elif(option == "2"):
        send_cpp(option); #option
    
        print( read_cpp() ); #texto ingresa matricula

        send_cpp( input("Matricula: ") ); #enviar matricula
    
        print( read_cpp() ); #Matricula eliminada
    
        print( read_cpp() ); #datos
        print( read_cpp() ); #datos
        print( read_cpp() ); #datos

    elif(option == "3"):

        send_cpp(option);
        
        for item in read_cpp():
            print(item);

    elif(option == "4"): #TODO maybe add cpp saving the data it has to a file? and then reloading it on boot?
        send_cpp(option);
        break; #Ends the while loop



process.terminate(); # Terminate the subprocess 
process.wait(); # Wait for the subprocess to exit