import requests

URL = "http://www.omdbapi.com/?s={}&apikey=95394772"

peli = input("Buscar: ")

respuesta = requests.get(URL.format(peli))


mijson = respuesta.json()

print(mijson.get("Search")[0].get("Title"))
print(mijson.get("Search")[0].get("Poster"))

print(mijson.get("Search")[1].get("Title"))
print(mijson.get("Search")[1].get("Poster"))
