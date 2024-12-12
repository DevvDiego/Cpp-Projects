import tkinter as tk
from pages.Page import Page
from pages.Mostrar import Mostrar

# imports only for type checking
from CppHandler import CppHandler 
from MySQLHandler import MySqlHandler 

class Modificar(Page):
    def __init__(self, frameContainer, mostrarWidget:Mostrar, cppHandler:CppHandler, mysqlHandler:MySqlHandler):
        super().__init__(frameContainer, mostrarWidget, cppHandler, mysqlHandler)

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()

    def configWidgets(self):
        self.title.config(
            text="Modificar".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13",fg="white",
        )

        self.inputPlateLabel.config(text="Matricula", font=("Roboto", 12))
        self.inputPlate.config(textvariable=self.plate)

        self.inputSpotLabel.config(text="Plaza", font=("Roboto", 12))
        self.inputSpot.config(textvariable=self.spot)

        self.inputPlateReplaceLabel.config(text="Matricula reemplazo", font=("Roboto", 12))
        self.inputPlateReplace.config(textvariable=self.plateReplace)

        self.inputSpotReplaceLabel.config(text="Plaza reemplazo", font=("Roboto", 12))
        self.inputSpotReplace.config(textvariable=self.spotReplace)

        self.btnEnviar.config(
            text="Aceptar", font=("Verdana", 10),
            padx=5, pady=5, command=self.sendData
        )

    def placeWidgets(self):
        self.title.pack(fill="x")
        
        self.inputPlateLabel.pack(pady=(40,0))
        self.inputPlate.pack()
        
        self.inputSpotLabel.pack(pady=(40,0))
        self.inputSpot.pack()

        self.inputPlateReplaceLabel.pack(pady=(40,0))
        self.inputPlateReplace.pack()

        self.inputSpotReplaceLabel.pack(pady=(40,0))
        self.inputSpotReplace.pack()

        self.spacer.pack()

        self.btnEnviar.pack()

    def createWidgets(self):
        self.title = tk.Label(self.frame)

        self.plate = tk.StringVar()
        self.inputPlateLabel = tk.Label(self.frame)
        self.inputPlate = tk.Entry(self.frame)

        self.spot = tk.StringVar()
        self.inputSpotLabel = tk.Label(self.frame)
        self.inputSpot = tk.Entry(self.frame)

        self.spotReplace = tk.StringVar()
        self.inputSpotReplaceLabel = tk.Label(self.frame)
        self.inputSpotReplace = tk.Entry(self.frame)

        self.plateReplace = tk.StringVar()
        self.inputPlateReplaceLabel = tk.Label(self.frame)
        self.inputPlateReplace = tk.Entry(self.frame)

        self.spacer = tk.Label(self.frame)

        self.btnEnviar = tk.Button(self.frame)

    def getFrame(self):
        return self.frame

    def sendData(self):

        #salida operations to erase from cpp and db
        result = self.cppHandler.salida(
            self.plateReplace.get() + "," + self.spotReplace.get()
        )
  
        if(result["status"] == "success"):
            
            self.mysqlHandler.delete(
                (self.plate.get() , )
            )
            
            #update after errasing
            self.updateMostrar()
        
        elif(result["status"] == "error"):
            print("error found in cpp")
            print(result)


        result = self.cppHandler.insertar(
            self.plateReplace.get() + "," + self.spotReplace.get()
        )

        if(result["status"] == "success"):
            self.updateMostrar()
            self.saveToMySql()
        
        elif(result["status"] == "error"):
            print("error found in cpp")
            print(result)



    def updateMostrar(self):
        self.mostrarWidget.updateText(
            text=self.cppHandler.mostrar()
        )

    def saveToMySql(self):
        self.mysqlHandler.insert(
            (self.plateReplace.get(), self.spotReplace.get())
        )