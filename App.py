from Gui import gui 
from CppHandler import CppHandler

cpp = CppHandler()

gui(cppHandler=cpp)


# After the tkinter gui has been killed, the subprocess might still be
# running in the background
cpp.endProgram() # Salida del subproceso