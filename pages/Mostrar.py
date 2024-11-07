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
            text="Parking".capitalize(), font=("Roboto", 15),
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
    
    def updateText(self, text:str):
        # enable to be able to insert text, disable to disable writing on it
        self.text.config(state="normal")

        self.text.delete("1.0",tk.END)
        self.text.insert(
            index=tk.END, 
            chars=self.parseText(text)
        )
        

        self.text.config(state="disabled")

    def parseText(self, text:str):
        return text.replace(",", "\n")