from bs4 import BeautifulSoup
import requests

from MD.scraper import ScrapeMD

statesites = [
	{'state': 'MD', 'url': 'http://emaryland.buyspeed.com/bso/external/publicBids.sdo'},
	] 

loader = ScrapeMD(statesites[0]['url'])
loader.StateScrape()