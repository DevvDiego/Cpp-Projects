import tkinter as tk
from pages.Mostrar import Mostrar

# imports only for type checking
from CppHandler import CppHandler 
from MySQLHandler import MySqlHandler 

#Keep recieving the handlers from outer class
#to just keep one instance of them running

class Page:

    def __init__(self, frameContainer, mostrarWidget:Mostrar, cppHandler:CppHandler, mysqlHandler:MySqlHandler ):
        self.frame = tk.Frame(frameContainer)
        
        self.mostrarWidget = mostrarWidget
        self.cppHandler = cppHandler
        self.mysqlHandler = mysqlHandler

    def getFrame(self):
        return self.frame