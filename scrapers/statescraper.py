from bs4 import BeautifulSoup
import requests

from MD.scraper import ScrapeMD

statesites = {'MD' : 'http://emaryland.buyspeed.com/bso/external/publicBids.sdo',
				'PA' : 'http://google.com',
}


	
'''SCRAPE MARYLAND'''
loader = ScrapeMD(statesites['MD'])
loader.StateScrape()
'''SCRAPE MARYLAND'''
