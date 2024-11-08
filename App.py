from Gui import gui 
from CppHandler import CppHandler
from MySQLHandler import MySqlHandler

cpp = CppHandler()
mysql = MySqlHandler()

gui(

    cppHandler=cpp,
    dbHandler=mysql,

)


# After the tkinter gui has been killed




# Kill the subprocess
# running in the background
# by using its own end
cpp.endProgram();