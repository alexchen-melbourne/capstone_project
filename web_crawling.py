import bs4 as bs
from bs4 import BeautifulSoup as Soup
import csv, requests
import time

# extra function
def extraDivCard(div):
    # sold date
    try:
        solddate = div.find('span', class_='listing-result__tag is-sold').get_text()
    except:
        solddate = None

    #sold price
    try:
        pricetag = div.find('p', class_='listing-result__price')
        price = pricetag.find('span').text
    except:
        price = None

    # property address 1
    try:
        addresstag = div.find('div', class_='listing-result__address-line-1')
        address1 = addresstag.find('span').text
    except:
        address1 = None

    try:
        addresstag2 = div.find('div', class_='listing-result__address-line-2')
        address2 = addresstag2.text
    except:
        address2 = None

    print address1, address2

    # post code
    try:
        postcode = div.find(itemprop="postalCode").get_text()
    except:
        postcode = None

    # geo location
    try:
        latitude = div(itemprop="latitude")[0]['content']
        longitude = div(itemprop="longitude")[0]['content']
    except:
        latitude, longitude = None, None

    # number of bedroom carpark bathroom
    try:
        bedsbathparking = div.find_all('span', class_='property-feature__feature-text-container')
        roomlist = []
        for bbp in bedsbathparking:
            roomlist.append(bbp.get_text())
        [bedrooms, bathrooms, carparkings] = roomlist
    except:
        bedrooms, bathrooms, carparkings = None, None, None

    # agent name
    try:
        agentbrand = div.find('span', class_='listing-result__agent-name').get_text()
    except:
        agent1 = div.find('div', class_='listing-result__brand-lazy')
        agent2 = div.find('div', class_='listing-result__brand')

        if agent1 != None:
            agentbrand = agent1.find('img', alt=True)['alt']
        elif agent2 != None:
            agentbrand = agent2.find('img', alt=True)['alt']
        else:
            agentbrand = None

    result = [solddate, price, address1, address2, postcode, latitude, longitude,
            bedrooms, bathrooms, carparkings, agentbrand]

    return result

# loop through one page
def onepage(url, writer):
    source = requests.get(url)
    text = source.text.encode('utf-8').decode('ascii', 'ignore')
    soup = bs.BeautifulSoup(text, 'lxml')

    cardlike_div = soup.find('ul', class_='search-results__results')
    if cardlike_div != None:
        c = cardlike_div.find_all('li', class_='search-results__listing')
        for div in cardlike_div.find_all('li', class_='search-results__listing'):
            ad = div.find('div', class_='adspot__wrapper')
            if ad == None:
                writer.writerow(extraDivCard(div))


# ----------------- main loop --------------------------

# attribute setup
bedrooms = ['0', '1', '2', '3', '4-any']
carspace = ['0', '1', '2-any']
postcodes = range(3000, 4000)
base_url = 'https://www.domain.com.au/sold-listings/?'

with open('data/houses.csv','wb') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['solddate', 'price', 'address1', 'address2', 'postcode', 'latitude', 'longitude', 'bedrooms', 'bathrooms', 'carparkings', 'agentbrand'])

    # loop through posrcodes
    for post in postcodes:
        for bed in bedrooms:
            for car in carspace:
                # find paginator
                url = base_url + 'bedrooms=' + bed + '&carspaces=' + car + '&ssubs=1&postcode=' + str(post) #+ '&page='
                response = requests.get(url)
                soup = Soup(response.text, 'lxml')
                paginator = []
                for div in soup.find_all('a', class_='paginator__page-button'):
                    paginator.append(int(div.text))

                # loop
                if paginator != []:
                    totalpage = max(paginator)
                    #print totalpage
                    for p in range(totalpage):
                        url_sub = url + '&page=' + str(p+1)
                        print url_sub
                        onepage(url_sub, writer)
                        time.sleep(1)
