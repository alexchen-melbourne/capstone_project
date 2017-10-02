from bs4 import BeautifulSoup as Soup
import csv, requests, time
import couchdb

def scrape_one_page(url):
    result = {}
    with requests.Session() as session:
        response = session.post(url, data={'start':0})
        soup = Soup(response.content, 'lxml')

        # left wrap
        left = soup.find('div', class_='left-wrap')

        result['date'] = left.find('span', class_='status-label label-sold').text.strip().encode('ascii','ignore')
        result['address'] = left.find('h1').text.strip().encode('ascii','ignore')
        result['price'] = left.find('span', class_='h4 pricedisplay truncate-single').text.strip().encode('ascii','ignore')

        # right wrap
        right = soup.find('div', class_='listing-features alt').text
        result['bed'] = right.split()[0].encode('ascii','ignore')
        result['bath'] = right.split()[2].encode('ascii','ignore')
        result['park'] = right.split()[4].encode('ascii','ignore')

        # land
        try:
            result['landsize'] = soup.find('ul', class_='list-horizontal details cfix ').text.strip().encode('ascii','ignore')
        except:
            result['landsize'] = None

        # title
        result['title'] = soup.find('h4', class_='h5 lowlight').text.encode('ascii','ignore')

        # description
        des = soup.find('div', id='description')
        descriptions = des.find('pre').text.split('\n')
        descrip = ''
        for d in descriptions:
            if ':' in d:
                try:
                    ele = d.split(': ')
                    result[ele[0].encode('ascii','ignore')] = ele[1].encode('ascii','ignore')
                except:
                    continue
            else:
                descrip += d
        result['description'] = descrip.encode('ascii','ignore')

        # feature
        feature = soup.find_all('ul', class_='list-vertical')
        for f in feature:
            try:
                result['property_type'] = f.find('strong').text.encode('ascii','ignore')
            except:
                result['features'] = f.text.encode('ascii','ignore').strip().split('\n')

    return result


# loop through one page
def onepage(url, db):
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
                result = scrape_one_page(href)
                time.sleep(1)
                result['link'] = href
                result['latitude'] = latitude
                result['longitude'] = longitude

                db.save(doc)
                print 'Saved one entry.'
            except:
                continue


# main

# suburbs
suburbs = []
with open('data/suburb_region.csv', 'r') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        new = ''.join(row[:-1])
        split = new.split()
        suburbs.append('-'.join(split[:-1] + ['vic'] + split[-1:]))

# attribute setup
bedrooms = ['1', '2', '3', '4', '5']
bathrooms = ['1', '2', '3']
carspace = ['0', '1', '2']

# https://www.domain.com.au/sold-listings/?bedrooms=2&bathrooms=1&carspaces=1&suburb=Kensington-vic-3031
base_url = 'https://www.domain.com.au/sold-listings/?'

couch = couchdb.Server()
db = couch['dsi']

# loop through posrcodes
for sub in suburbs:
    for bed in bedrooms:
        for car in carspace:
            # find paginator
            url = base_url + 'bedrooms=' + bed + '&carspaces=' + car + '&suburb=' + sub
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
                    onepage(url_sub, db)
