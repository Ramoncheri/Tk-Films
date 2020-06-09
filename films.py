from tkinter import *
from tkinter import ttk
import requests
from configparser import *
from PIL import Image, ImageTk
from io import BytesIO

config= ConfigParser()
config.read('config.ini')


APIKEY= config["OMDB_API"]["APIKEY"]
URL = "http://www.omdbapi.com/?s={}&apikey={}"

class Searcher(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent)

        lblSearcher= ttk.Label(self, text="Pelicula:")
        self.ctrSearcher= StringVar()
        txtSearcher= ttk.Entry(self, width=30, textvariable= self.ctrSearcher)
        btnSearcher= ttk.Button(self, text="Buscar", command= lambda:command(self.ctrSearcher.get()))

        lblSearcher.pack(side= LEFT)
        txtSearcher.pack(side= LEFT)
        btnSearcher.pack(side= LEFT)

    #def click(self):
        #print(self.ctrSearcher.get())

class Controller(ttk.Frame):

    def __init__(self, parent):
        ttk. Frame.__init__(self, parent, width= 400, height= 550)
        self.grid_propagate(False)

        self.searcher= Searcher(self, self.busca)
        self.searcher.grid(column=0, row=0)

        self.film= Film(self)
        self.film.grid(column=0, row=1)

        self.botones= Botones(self, self.siguiente)
        self.botones.grid(column=0, row= 2)
        self.films={}
        self.n=1

        
    def busca(self, peli):
        print(peli)
        url= URL.format(peli, APIKEY)
        results= requests.get(url)

        if results.status_code== 200:
            self.films= results.json()

            if self.films.get("Response")== "True":
                result_peli= self.films.get("Search")[0]
                peli_a_mostrar={"titulo":result_peli.get("Title"),"anno": result_peli.get("Year"), "poster": result_peli.get("Poster")}
                self.film.mostrada= peli_a_mostrar  #este 'mostrada' viene del atributo oculto y del getter y setter de Film
               
        return self.films   
        

    def siguiente(self):
        
        
        result_peli= self.films.get("Search")[self.n]
        peli_a_mostrar={"titulo":result_peli.get("Title"),"anno": result_peli.get("Year"), "poster": result_peli.get("Poster")}
        self.film.mostrada= peli_a_mostrar
        self.film= Film(self)
        self.film.grid(column=0, row=1)
        self.n += 1
            


   
    def prueba(self):
        print('prueba')

    
class Film(ttk.Frame):

    __mostrada= None
    __mostrada1= None
    
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.lblTitle= ttk.Label(self, text="Titulo")
        self.lblYear= ttk.Label(self, text= "1900")
        self.image= Label(self)
        self.photo= None

        

        self.image.pack(side= TOP)
        self.lblTitle.pack(side=TOP)
        self.lblYear.pack(side= TOP)
        

    @property
    def mostrada(self):
        return(self.__mostrada)

    @mostrada.setter
    def mostrada(self, value):  #value es un dict con titulo, año y poster
        self.__mostrada = value

        self.lblTitle.config(text= self.__mostrada.get("titulo"))
        self.lblYear.config(text= self.__mostrada.get("anno"))

        
        if self.__mostrada.get("poster")== "N/A":
            return
        
        r= requests.get(self.__mostrada.get("poster"))
        if r.status_code== 200:
            bimage= r.content
            image= Image.open(BytesIO(bimage))
            self.photo= ImageTk.PhotoImage(image)

            self.image.config(image= self.photo)
            self.image.image= self.photo

        
    
    

    
class Botones(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent)

        self.btn_volver= ttk.Button(self, text="Volver", command= None)
        self.btn_siguiente= ttk.Button(self, text="Siguiente", command= command)

        self.btn_volver.pack(side= LEFT)
        self.btn_siguiente.pack(side= RIGHT)
    
    

