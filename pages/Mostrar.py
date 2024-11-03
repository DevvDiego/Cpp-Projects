import tkinter as tk
from tkinter import scrolledtext

class Mostrar:

    def __init__(self, frameContainer):
        self.frame = tk.Frame(frameContainer)

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()

    def configWidgets(self):
        self.title.config(
            text="Ingresar".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13", fg="white",
        )


        # ? make it fixed size or responsive
        self.text.config(
            font=("Roboto", 10), bg="gray8" , fg="white", cursor="",
            wrap=tk.WORD, width=30,
            state=tk.DISABLED,
        )


    def placeWidgets(self):

        self.title.pack(fill="x")
        self.text.pack(fill="none", expand=None)

    def createWidgets(self):

        self.title = tk.Label(self.frame)
        self.text = scrolledtext.ScrolledText(self.frame)
        

    def getFrame(self):
        return self.frame