import tkinter as tk


class gui:


    def show(self, frame):
        frame.lift()
        self.buttonframe.lift()


    def configWidgets(self):
        self.root.geometry("500x450")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        # self.root.config(bg="black")
        # self.buttonframe.config(bg="")
        self.resultContainer.config(bg="gray13", width=190)

        self.label.config(
            text="Ingresar".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13", fg="white",
        )
        self.label2.config(
            text="Salida".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13", fg="white",
        )
        self.label3.config(
            text="Mostrar".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13", fg="white",
        )
        self.label4.config(
            text="Guardar".capitalize(), font=("Roboto", 15),
            height=2, bg="gray13", fg="white",
        )



        self.btn_ingresar.config(
            text="Ingresar", width=8, cursor="hand2",
            command=lambda: self.show(self.pag_ingresar)
        )
        self.btn_salida.config(
            text="Salida",  width=8, cursor="hand2",
            command=lambda: self.show(self.pag_salida)
        )
        self.btn_mostrar.config(
            text="Mostrar", width=8, cursor="hand2",
            command=lambda: self.show(self.pag_mostrar)
        )
        self.btn_guardar.config(
            text="Guardar", width=8, cursor="hand2", 
            command=lambda: self.show(self.pag_guardar)
        )
        
    def placeWidgets(self):
        self.container.grid(row=0,column=0, sticky="nswe",)
        self.resultContainer.grid(row=0, column=1, sticky="nswe")
        self.buttonframe.grid(row=1, column=0, sticky="swe")

        self.label.pack(fill="x",  )
        self.label2.pack(fill="x", )
        self.label3.pack(fill="x", )
        self.label4.pack(fill="x", )

        self.pag_ingresar.place(x=0, y=0, relwidth=1, relheight=1)
        self.pag_salida.place(x=0, y=0, relwidth=1, relheight=1)
        self.pag_mostrar.place(x=0, y=0, relwidth=1, relheight=1)
        self.pag_guardar.place(x=0, y=0, relwidth=1, relheight=1)

        self.btn_ingresar.pack(side="left", padx=(0,5))
        self.btn_salida.pack(side="left", padx=(0,5))
        self.btn_mostrar.pack(side="left", padx=(0,5))
        self.btn_guardar.pack(side="left", padx=(0,5))

    def createWidgets(self):
        self.root = tk.Tk()
        # self.root.wm_attributes('-transparentcolor', 'white')


        self.container = tk.Frame(self.root, width=10)
        self.resultContainer = tk.Frame(self.root)
        self.buttonframe = tk.Frame(self.container)

        self.btn_ingresar = tk.Button(self.buttonframe)
        self.btn_salida = tk.Button(self.buttonframe)
        self.btn_mostrar = tk.Button(self.buttonframe)
        self.btn_guardar = tk.Button(self.buttonframe)


        self.pag_ingresar = tk.Frame(self.container)
        self.label = tk.Label(self.pag_ingresar)

        self.pag_salida = tk.Frame(self.container)
        self.label2 = tk.Label(self.pag_salida)

        self.pag_mostrar = tk.Frame(self.container)
        self.label3 = tk.Label(self.pag_mostrar)

        self.pag_guardar = tk.Frame(self.container)
        self.label4 =tk.Label(self.pag_guardar)
        
        # self.pageOneLeftFrame = tk.Frame(self.pag_ingresar)
        # self.pageOneRightFrame = tk.Frame(self.pag_ingresar)




    def __init__ (self):

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()


        self.show(self.pag_ingresar)

        self.root.mainloop()


gui()