import googlemaps
import unicodedata
import pandas as pd
import numpy as np
import time, csv

key = 'AIzaSyDFEspHpWIgzaTPWwiAi9jtZgSktjTfH5A'
gmaps = googlemaps.Client(key)

CBD = (-37.817860, 144.965855)

# define function to calc distance and find nesarest spot
def getDistance(origins, destinations):
    try:
        matrix = gmaps.distance_matrix(origins, destinations, mode="driving")

        distance = matrix['rows'][0]['elements'][0]['distance']['text'].encode('ascii','ignore')
        seconds = matrix['rows'][0]['elements'][0]['distance']['value']
        mini = matrix['rows'][0]['elements'][0]['duration']['text'].encode('ascii','ignore')

        return distance, seconds, mini
    except:
        return 'error'

def findNearest(location, keyword):
    # radius: metres
    result = gmaps.places_nearby(location=location, keyword=keyword, radius=5000)
    if len(result['results']) > 0:
        # 1st result is nearest
        spot = (result['results'][0]['geometry']['location']['lat'],
                result['results'][0]['geometry']['location']['lng'])
    else:
        spot = 'None finding'
    return spot

def findNoOfInterest(location, keyword):
    result = gmaps.places_nearby(location=location, keyword='mcdonalds', radius=5000)
    return len(result['results'])

# main
with open('data/houses.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
