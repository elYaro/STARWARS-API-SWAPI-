import requests
import json

# connect to SWAPI server and get 10 planets data
# gives back dictionary
def giveMeTenPlanets():
    url = "https://swapi.co/api/planets/?page=2"
    tenPlanets = requests.get(url).json()
    return tenPlanets


# connect to SWAPI server and get 10 previous planets data
# gives back dictionary
def giveMeTenPreviousPlanets(urlTo10PreviousPlanets):
    url = urlTo10PreviousPlanets
    tenPreviousPlanets = requests.get(url).json()
    return tenPreviousPlanets