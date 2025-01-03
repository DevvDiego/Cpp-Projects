import tkinter as tk
from pages.Mostrar import Mostrar

# imports only for type checking
from CppHandler import CppHandler 
from MySQLHandler import MySqlHandler 

class Salida:

    def __init__(self, frameContainer, mostrarWidget:Mostrar, cppHandler:CppHandler, mysqlHandler:MySqlHandler):

        self.mostrarWidget = mostrarWidget

        self.cppHandler = cppHandler
        self.mysqlHandler = mysqlHandler
        self.frame = tk.Frame(frameContainer)

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()

    def configWidgets(self):
        self.title.config(
            text="Salida".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13",fg="white",
        )

        self.inputPlateLabel.config(text="Ingresa la matricula", font=("Roboto", 12))
        self.inputPlate.config(textvariable=self.plate)

        self.spacer.config(text="", pady=20)

        # TODO: add way that after clicking, the right dark side of the root frame, shows the parking
        # self.btnEnviar.bind()
        self.btnEnviar.config(
            text="Aceptar", font=("Verdana", 10),
            padx=5, pady=5, command=self.sendData
        )

    def placeWidgets(self):
        self.title.pack(fill="x")
        
        self.inputPlateLabel.pack(pady=(40,0))
        self.inputPlate.pack()

        # self.inputSpotLabel.pack(pady=(40,0))
        # self.inputSpot.pack()

        self.spacer.pack()

        self.btnEnviar.pack() 

    def createWidgets(self):
        self.title = tk.Label(self.frame)

        self.plate = tk.StringVar()
        self.inputPlateLabel = tk.Label(self.frame)
        self.inputPlate = tk.Entry(self.frame)

        # self.spot = tk.StringVar()
        # self.inputSpotLabel = tk.Label(self.frame)
        # self.inputSpot = tk.Entry(self.frame)

        self.spacer = tk.Label(self.frame)

        self.btnEnviar = tk.Button(self.frame)

        # self.btn = tk.Button(self.frame, text="Mandar", command=lambda: print(self.matricula.get()))

    def getFrame(self):
        return self.frame

    def sendData(self):
        result = self.cppHandler.salida(
            self.plate.get()
        )

        if(result["status"] == "success"):
            self.updateMostrar()
            self.deleteFromMySql()
        
        elif(result["status"] == "error"):
            print("error found in cpp")
            print(result)

    def updateMostrar(self):
        self.mostrarWidget.updateText(
            text=self.cppHandler.mostrar()
        )

    def deleteFromMySql(self):
        self.mysqlHandler.delete(
            (self.plate.get() , ) #! use a comma to make it a real tuple
        )

        