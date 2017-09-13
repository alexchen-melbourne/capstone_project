import googlemaps
import csv
import simplejson, urllib

# key = 'AIzaSyDFEspHpWIgzaTPWwiAi9jtZgSktjTfH5A'
# gmaps = googlemaps.Client(key)
#
# CBD = (-37.810817, 144.963135)
CBD = '-37.810817,%20144.963135'

# define function to calc distance and find nesarest spot
def getDistance(origins, destinations):
    # matrix = gmaps.distance_matrix(origins, destinations, mode="driving")
    # distance = matrix['rows'][0]['elements'][0]['distance']['text']
    url = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origins +'&destinations=' + destinations + '&mode=driving&language=en-EN&sensor=false'
    result= simplejson.load(urllib.urlopen(url))

    distance = result['rows'][0]['elements'][0]['distance']['text']
    return distance

def findNearest(loc, key):
    # result = gmaps.places_nearby(location=loc, keyword=key, radius=5000)
    # if len(result['results']) > 0:
    #     spot = (result['results'][0]['geometry']['location']['lat'],
    #             result['results'][0]['geometry']['location']['lng'])
    # else:
    #     spot = 'None finding'
    return spot
#
# def findNoOfInterest(location, keyword):
#     result = gmaps.places_nearby(location=location, keyword=keyword, radius=5000)
#     return len(result['results'])

# main
with open('data/house1.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    with open('data/house1_add_info.csv','wb') as csv_file:
        # writer = csv.writer(csv_file, delimiter=',')
        # writer.writerow(['location', '2cbd', '2train',
        #                  'school', 'shopping_mall', 'cafe',
        #                  'atm', 'gas_station'])
        count = 0
        for row in reader:
            point = row[10]
            lat = point.split('\'')[1]
            lng = point.split('\'')[3]
            point = lat + '%20' + lng
            print point

            _2cbd = getDistance(point, CBD)

            # Calc distance
            # train = findNearest(point, 'train_station')
            # school = findNearest(point, 'school')
            # shopping_mall = findNearest(point, 'shopping_mall')
            #
            # _2train = getDistance(point, train)
            # _school = getDistance(point, school)
            # _shopping_mall = getDistance(point, shopping_mall)

            print _2cbd

            # # No of cafw, gas_station, atm
            # _cafe = findNoOfInterest(point, 'cafe')
            # _atm = findNoOfInterest(point, 'atm')
            # _gas_station = findNoOfInterest(point, 'gas_station')
            #
            # writer.writerow([point, _2cbd, _2train, _school,
            #                  _shopping_mall, _cafe,
            #                  _atm, _gas_station])
            count+=1
            print count
