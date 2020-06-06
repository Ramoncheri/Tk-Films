from tkinter import *
from tkinter import ttk
import requests


APIKEY= "95394772"
URL = "http://www.omdbapi.com/?s={}&apikey={}"

class Searcher(ttk.Frame):
    def __init__(self, parent, command):
        ttk.Frame.__init__(self, parent)

        lblSearcher= ttk.Label(self, text="Film:")
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

    def busca(self, peli):
        print(peli)
        url= URL.format(peli, APIKEY)
        results= requests.get(url)

        print(results.txt)

class Film(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.lblTitle= ttk.Label(self, text="Titulo")
        self.lblYear= ttk.Label(self, text= "1900")

        self.lblTitle.pack(side=TOP)
        self.lblYear.pack(side= TOP)
        

        
        

