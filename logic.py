import requests
import json

# connect to SWAPI server and get 10 planets data
# gives back dictionary
def giveMeTenPlanets():
    url = "https://swapi.co/api/planets/?page=1"
    tenPlanets = requests.get(url).json()
    return tenPlanets