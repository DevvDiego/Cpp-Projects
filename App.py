from Gui import gui 
from CppHandler import CppHandler
from MySQLHandler import MySqlHandler

sqlCredentials = {
    "host":"localhost",
    "database":"pysql",
    "user":"root",
    "password":"",
}

cpp = CppHandler()
mysql = MySqlHandler(sqlCredentials)

gui(

    cppHandler=cpp,
    mysqlHandler=mysql,

)


# After the tkinter gui has been killed




# Kill the subprocess
# running in the background
# by using its own end
cpp.endProgram();