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

    user_input = str(input("PYTHON Enter a command: "));
    
    if user_input.lower() == 'exit':

        send_cpp(user_input);
        print("CPP exit code: ", read_cpp());
        break

    if(user_input == "1"):
        send_cpp(user_input);

        send_cpp( input("Matricula: ") );

        send_cpp( input("Plaza: ") );

        print( read_cpp() )
        print( read_cpp() )
        print( read_cpp() )

    elif(user_input == "2"):
        send_cpp(user_input); #option
    
        print( read_cpp() ); #texto ingresa matricula

        send_cpp( input("Matricula: ") ); #enviar matricula
    
        print( read_cpp() ); #Matricula eliminada
    
        print( read_cpp() ); #datos
        print( read_cpp() ); #datos
        print( read_cpp() ); #datos

        
    elif(user_input == "3"):

        send_cpp(user_input);
        
        for item in read_cpp():
            print(item + "\n");



process.terminate(); # Terminate the subprocess 
process.wait(); # Wait for the subprocess to exit