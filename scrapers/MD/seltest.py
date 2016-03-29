import datetime
from selenium import webdriver
from bs4 import BeautifulSoup




class ScrapeMD(object):

	def __init__(self, url, browser):
		self.url = url
		self.browser = browser
		self.browser.get(self.url)
		self.numberOfContracts = self.GetNumberOfContracts()
		self.scraped_page_container = []
		self.output_file_name = "../htmloutput/MD/MDPage" + "-" + str(datetime.datetime.now()) + ".html"
		open(self.output_file_name, 'w').close()

		self.soup = []
		self.temp = None

		self.bs4container = []

	def GetNumberOfContracts(self):
		MDNumContracts = self.browser.find_element_by_xpath("/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[1]/td")
		MDNumContracts = MDNumContracts.get_attribute('innerHTML')
		MDNumContracts = str(MDNumContracts).rsplit(' ', 1)[1]
		return int(MDNumContracts)

	def IterateThroughMDPages(self):
		numberOfPages = self.numberOfContracts / 25
		for index in range(1,numberOfPages+2): #Why do I have to add the +2 to the number of pages to cover all of the pages.  I would understand +1, but wtf is up with +2
			try:
				# self.browser.find_element_by_xpath("/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[" + str(index) + "]").click()
				self.browser.execute_script("viewPage(" + str(index) + ")")
				self.browser.forward()
				# self.SaveToFile(self.browser.page_source, index)	#Switch on to write individual file for each Selenium Scraping Page 
				self.WriteToObject(self.browser.page_source)	#Appends to a list attribute															
			except:
				pass

	# def SaveToFile(self, scraped_data, index):
	# 	to_be_written = scraped_data.encode('utf8')

	# 	f = open("../htmloutput/MD/MDPage" + str(index) + "-" + str(datetime.datetime.now()) + ".html", 'w')
	# 	f.write(to_be_written)
	# 	f.close()

	def WriteToObject(self, scraped_data):
		#Appends each Selenium Scraping Page to a list for scraping by BS4
		to_be_written = scraped_data.encode('utf8')
		self.scraped_page_container.append(to_be_written)
		
		#Writes the Selenium Scrapings to a file for error checking
		f = open(self.output_file_name, 'a') 
		f.write(to_be_written)
		f.close()

	def ScrapeFiles(self):
		open('temp.html', 'w').close()

		#Takes each list element (which is a page from the website), and 
		for scrapedPage in self.scraped_page_container:
			soup = BeautifulSoup(scrapedPage, 'lxml')
			# self.bs4container.append(soup.find_all('tr', ['tableStripe-01', 'tableStripe-02']))
			for contractLine in soup.find_all('tr', ['tableStripe-01', 'tableStripe-02']):
				self.bs4container.append(contractLine)

		for listing in self.bs4container:
			f2 = open('temp.html', 'a')
			f2.write(str(listing))
			f2.close()

	# def WriteToDB(self):
	# 	for 



		#YOU MUST USE THE LXML PARSER FOR THESE TO WORK FOR SOME REASON
		#test = soup.find_all('tr', ['tableStripe-01', 'tableStripe-02'])
		#test = soup.find_all('True', {'class':['tableStripe-01', 'tableStripe-02']})


		# soup = BeautifulSoup(open(self.output_file_name), 'html.parser')
		# self.temp = soup
		# self.bs4container.append(soup.find_all('table'))





		#Need to scrape <table id="resultsTable" name="resultsTable" class="table-02">
		#Each row in the table reciprocates betwen the tableStripe classes as seen below
			#<tr class="tableStripe-01"><td class="tableText-01" align="center" valign="top">
			#<tr class="tableStripe-02"><td class="tableText-01" align="center" valign="top">
		#I think that each tableStripe has the same number of <td> elements



	def WriteToDatabase(self):
		pass







# temp = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[12]').click() #Find the link to the second page of contracts and click on it
# browser.forward() #Moves the object in browser to where the newly opened page is




# print browser.page_source #Used to test where the current browser object is

# '''DOWNLOAD FILE NOT WORKING'''
# results_url = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[1]').get_attribute('href')
# os.system('wget {}'.format(results_url))
# '''DOWNLOAD FILE NOT WORKING'''
