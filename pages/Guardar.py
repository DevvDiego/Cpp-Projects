import tkinter as tk


class Guardar:

    def __init__(self, frameContainer):
        self.frame = tk.Frame(frameContainer)

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()

    def configWidgets(self):
        self.title.config(
            text="Ingresar".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13",fg="white",
        )
        
        self.spacer.config(text="", pady=20)

        self.btnEnviar.config(
            text="Guardar en MySQL", font=("Verdana", 10),
            padx=5, pady=5, command=lambda: print("comando: guardar a mysql")
        )

    def placeWidgets(self):
        
        self.title.pack(fill="x")
        self.spacer.pack()
        self.btnEnviar.pack()

    def createWidgets(self):

        self.title = tk.Label(self.frame)
        self.spacer = tk.Label(self.frame)
        self.btnEnviar = tk.Button(self.frame)

    def getFrame(self):
        return self.frame
