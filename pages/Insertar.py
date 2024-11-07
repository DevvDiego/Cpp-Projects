import tkinter as tk
from CppHandler import CppHandler


class Insertar:

    def __init__(self, frameContainer, cppHandler:CppHandler):
        self.cppHandler = cppHandler
        self.frame = tk.Frame(frameContainer)

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()

    def configWidgets(self):
        self.title.config(
            text="Ingresar".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13",fg="white",
        )

        self.inputPlateLabel.config(text="Ingresa la matricula", font=("Roboto", 12))
        self.inputPlate.config(textvariable=self.plate)

        self.inputSpotLabel.config(text="Ingresa el lugar", font=("Roboto", 12))
        self.inputSpot.config(textvariable=self.spot)

        self.spacer.config(text="", pady=20)

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

        self.spacer = tk.Label(self.frame)

        self.btnEnviar = tk.Button(self.frame)

    def getFrame(self):
        return self.frame

    def sendData(self):
        self.cppHandler.insertar(self.plate.get() + "," + self.spot.get())