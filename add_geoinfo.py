import csv, simplejson, urllib, time

CBD = '-37.810817,%20144.963135'

# define function to calc distance and find nesarest spot
def getDistance(origins, destinations):
    url = 'http://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origins +'&destinations=' + destinations + '&mode=driving&language=en-EN&sensor=false'
    result= simplejson.load(urllib.urlopen(url))
    try:
        distance = result['rows'][0]['elements'][0]['distance']['text']
        return distance
    except Exception as e:
        print e
        return None

# main
with open('data/houses.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for i in range(1,1171):
        next(reader)

    with open('data/houses_add_info.csv','wb') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['location', '2cbd'])
        for row in reader:
            point = row[10]
            lat = point.split('\'')[1]
            lng = point.split('\'')[3]
            point = lat + '%20' + lng

            _2cbd = getDistance(point, CBD)
            print _2cbd
            writer.writerow([point, _2cbd])
