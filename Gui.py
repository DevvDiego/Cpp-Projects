import tkinter as tk
from pages.Guardar import Guardar 
from pages.Insertar import Insertar 
from pages.Mostrar import Mostrar 
from pages.Salida import Salida 


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

        self.resultContainer.config(bg="gray13", width=190)

        #! Not a page, but a section right side of the root frame
        self.pag_mostrar.config(bg="gray13")


        self.btn_ingresar.config(
            text="Ingresar", width=8, cursor="hand2",
            command=lambda: self.show(self.pag_insertar)
        )
        self.btn_salida.config(
            text="Salida",  width=8, cursor="hand2",
            command=lambda: self.show(self.pag_salida)
        )
        self.btn_guardar.config(
            text="Guardar", width=8, cursor="hand2", 
            command=lambda: self.show(self.pag_guardar)
        )
        
    def placeWidgets(self):
        self.container.grid(row=0,column=0, sticky="nswe",)
        self.resultContainer.grid(row=0, column=1, sticky="nswe")
        self.buttonframe.grid(row=1, column=0, sticky="swe")

        #! Not a page, but a section right side of the root frame
        self.pag_mostrar.pack(fill="x", padx=10)


        self.pag_insertar.place(x=0, y=0, relwidth=1, relheight=1)
        self.pag_salida.place(x=0, y=0, relwidth=1, relheight=1)
        self.pag_guardar.place(x=0, y=0, relwidth=1, relheight=1)

        self.btn_ingresar.pack(side="left", padx=(0,5))
        self.btn_salida.pack(side="left", padx=(0,5))
        # self.btn_mostrar.pack(side="left", padx=(0,5)) #CHECK createWidgets
        self.btn_guardar.pack(side="left", padx=(0,5))

    def createWidgets(self):
        self.root = tk.Tk()
        # self.root.wm_attributes('-transparentcolor', 'white')


        self.container = tk.Frame(self.root, width=10)
        self.resultContainer = tk.Frame(self.root)
        self.buttonframe = tk.Frame(self.container)



        self.btn_ingresar = tk.Button(self.buttonframe)
        self.btn_salida = tk.Button(self.buttonframe)
        # ? self.btn_mostrar = tk.Button(self.buttonframe) #remove button? "dynamic" reload?
        self.btn_guardar = tk.Button(self.buttonframe)



        self.mostrar = Mostrar(
            frameContainer=self.resultContainer
        )
        self.pag_mostrar = self.mostrar.getFrame()


        self.insertar = Insertar(
            frameContainer=self.container, 
            mostrarWidget=self.mostrar, 
            cppHandler=self.cppHandler
        )
        self.pag_insertar = self.insertar.getFrame()
        
        
        self.salida = Salida(
            frameContainer=self.container,
            mostrarWidget=self.mostrar,
            cppHandler=self.cppHandler
        )
        self.pag_salida = self.salida.getFrame()


        # TODO make saving to a mysql BDD
        self.guardar = Guardar(
            frameContainer=self.container
        )
        self.pag_guardar = self.guardar.getFrame()



# TODO create the menu for each option and add a button to send data and recieve
    def __init__ (self, cppHandler):

        self.cppHandler = cppHandler

        self.createWidgets()
        self.configWidgets()
        self.placeWidgets()


        self.show(self.pag_insertar)

        self.root.mainloop()
