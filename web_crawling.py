import bs4 as bs
import urllib2

sourcepage = 'https://www.domain.com.au/sold-listings/melbourne-vic-3000/?ssubs=1&suburb=melbourne-vic-3000&page=1'
source = urllib2.urlopen(sourcepage).read()

soup = bs.BeautifulSoup(source, 'lxml')

cardlike_div = soup.select('.search-results__listing')
c = 0
for div in cardlike_div:
    try:
        date = div.find('span', class_='listing-result__tag is-sold').get_text()
        price = div.find('p', class_='listing-result__price')
        address = div.find('div', class_='listing-result__address-line-1')
        post = div.find(itemprop="postalCode").get_text()
        latitude = div(itemprop="latitude")[0]['content']
        longitude = div(itemprop="longitude")[0]['content']

        bedsbathparking = div.find_all('span', class_='property-feature__feature-text-container')
        roomlist = []
        for i in bedsbathparking:
            roomlist.append(i.get_text())
        [beds, baths, cars] = roomlist
        bed = beds.split()[0]
        bath = baths.split()[0]
        car = cars.split()[0]

        #print date
        #print price.find('span').text
        #print address.find('span').text
        #print post
        #print latitude
        #print longitude
        #print bed, bath, car

        print '---- {} ------'.format(c)
        c+=1
    except AttributeError:
        continue
