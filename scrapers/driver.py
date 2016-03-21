from bs4 import BeautifulSoup
import requests

from MD.scraper import ScrapeMD

#This needs to be moved to a database (or should it, how much slower would it be?)
statesites = {'MD' : 'http://emaryland.buyspeed.com/bso/external/publicBids.sdo',
				'PA' : 'http://google.com',
}


	
'''SCRAPE MD'''
loader = ScrapeMD(statesites['MD'])
loader.StateScrape()
'''SCRAPE MD'''

'''SCRAPE PA
