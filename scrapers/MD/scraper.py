import requests
from bs4 import BeautifulSoup



class ScrapeMD(object):

	def __init__(self, url):
		self.url = url
		self.r = requests.get(self.url)
		self.data = self.r.text
		self.soup1 = str(BeautifulSoup(self.data, "html.parser"))

	def StateScrape(self):
		# r = requests.get(self.url)
		# data = r.text

		# soup1 = str(BeautifulSoup(data, "html.parser"))
		# soup2 = str(BeautifulSoup("<html>data</html>"))


		f = open('../htmloutput/MD.html', 'w')
		f.write(self.soup1)
		f.close()