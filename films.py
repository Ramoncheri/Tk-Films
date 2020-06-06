from tkinter import *
from tkinter import ttk
import requests
from configparser import *

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

    def click(self):
        print(self.ctrSearcher.get())

class Controller(ttk.Frame):

    def __init__(self, parent):
        ttk. Frame.__init__(self, parent, width= 400, height= 550)
        self.grid_propagate(False)

        self.searcher= Searcher(self, self.busca)
        self.searcher.grid(column=0, row=0)

        self.film= Film(self)
        self.film.grid(column=0, row=1)

    def busca(self, peli):
        print(peli)
        url= URL.format(peli, APIKEY)
        results= requests.get(url)

        if results.status_code== 200:
            films= results.json()
            if films.get("Response")== "True":
                result_peli= films.get("Search")[0]
                peli_a_mostrar={"titulo":result_peli.get("Title"),"anno": result_peli.get("Year"), "poster": result_peli.get("Poster")}
                self.film.mostrada= peli_a_mostrar  #este 'mostrada' viene del atributo oculto y del getter y setter de Film


        print(results.text)
    
class Film(ttk.Frame):

    __mostrada= None
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.lblTitle= ttk.Label(self, text="Titulo")
        self.lblYear= ttk.Label(self, text= "1900")

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
        

        
        

