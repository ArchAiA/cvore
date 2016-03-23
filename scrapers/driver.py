from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from MD.seltest import ScrapeMD


browser = webdriver.Chrome(executable_path = '../dependencies/chromedriver')

#This needs to be moved to a database (or should it, how much slower would it be?)
statesites = {'MD' : 'http://emaryland.buyspeed.com/bso/external/publicBids.sdo',
				'PA' : 'http://google.com',
}


	
'''SCRAPE MD'''
loader = ScrapeMD(statesites['MD'], browser)
loader.IterateThroughMDPages()
# loader.StateScrape()

'''SCRAPE MD'''

'''SCRAPE PA'''
