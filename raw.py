from bs4 import BeautifulSoup as Soup
import csv, requests, time

def scrape_one_page(url, latitude, longitude, href, writer):
# 'price', 'landsize', 'address', 'park', 'bed',
# 'bath', 'longitude', 'latitude', 'date', \\\

    response = requests.get(url)
    soup = Soup(response.content, 'lxml')
    try:
        landsize = soup.find('ul', class_='list-horizontal details cfix ').text.strip().encode('ascii','ignore')
    except:
        return None

    with requests.Session() as session:
        response = session.post(url, data={'start':0})
        soup = Soup(response.content, 'lxml')

        # left wrap
        left = soup.find('div', class_='left-wrap')

        date = left.find('span', class_='status-label label-sold').text.strip().encode('ascii','ignore')
        address = left.find('h1').text.strip().encode('ascii','ignore')
        price = left.find('span', class_='h4 pricedisplay truncate-single').text.strip().encode('ascii','ignore')

        # right wrap
        right = soup.find('div', class_='listing-features alt').text
        bed = right.split()[0].encode('ascii','ignore')
        bath = right.split()[2].encode('ascii','ignore')
        park = right.split()[4].encode('ascii','ignore')

    try:
        writer.writerow([price,landsize, address, park, bed, bath, longitude, latitude, date])
        print 'success one!'
    except:
        print 'error'


# loop through one page
def onepage(url, writer):
    source = requests.get(url)
    text = source.text.encode('utf-8').decode('ascii', 'ignore')
    soup = Soup(text, 'lxml')

    cardlike_div = soup.find('ul', class_='search-results__results')
    if cardlike_div != None:
        cards = cardlike_div.find_all('li', class_='search-results__listing')
        for c in cards:
            try:
                link = c.find('a', class_='listing-result__address')
                latitude = c(itemprop="latitude")[0]['content']
                longitude = c(itemprop="longitude")[0]['content']
                href = link.get('href')
                scrape_one_page(href, latitude, longitude, href, writer)
            except:
                continue


# main

# suburbs
suburbs = []
with open('data/suburb_region.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        new = ''.join(row[:-1])
        split = new.split()
        suburbs.append('-'.join(split[:-1] + ['vic'] + split[-1:]))

print 'suburb load done'

# attribute setup
bedrooms = ['2', '3']
bathrooms = ['1', '2']
carspace = ['0', '1']

# https://www.domain.com.au/sold-listings/?bedrooms=2&bathrooms=1&carspaces=1&suburb=Kensington-vic-3031
base_url = 'https://www.domain.com.au/sold-listings/?'
columns = ['price', 'landsize', 'address', 'park', 'bed', 'bath', 'longitude', 'latitude', 'date', 'property_type']

with open('raw.csv','wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(columns)
    # loop through posrcodes
    for sub in suburbs:
        for bed in bedrooms:
            for car in carspace:
                # find paginator
                url = base_url + 'bedrooms=' + bed + '&carspaces=' + car + '&suburb=' + sub
                print url
                response = requests.get(url)
                soup = Soup(response.text, 'lxml')
                paginator = []
                for div in soup.find_all('a', class_='paginator__page-button'):
                    paginator.append(int(div.text))

                # loop
                if paginator != []:
                    totalpage = max(paginator)
                    for p in range(totalpage):
                        url_sub = url + '&page=' + str(p+1)
                        print url_sub
                        onepage(url_sub, writer)

