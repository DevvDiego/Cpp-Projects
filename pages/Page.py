import tkinter as tk
from pages.Mostrar import Mostrar

# imports only for type checking
from CppHandler import CppHandler 
from MySQLHandler import MySqlHandler 

class Page:

    def __init__(self, frameContainer, mostrarWidget:Mostrar, cppHandler:CppHandler, mysqlHandler:MySqlHandler ):
        self.mostrarWidget = mostrarWidget
        self.cppHandler = cppHandler
        self.mysqlHandler = mysqlHandler
        self.frame = tk.Frame(frameContainer)

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()

    def configWidgets(self):
        pass

    def placeWidgets(self):
        pass

    def createWidgets(self):
        pass

    def getFrame(self):
        return self.frame

    def sendData(self):
        pass

    def updateMostrar(self):
        pass

    def saveToMySql(self):
        pass