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
		for item in self.scraped_page_container:
			soup = BeautifulSoup(item, 'html.parser')
			self.bs4container.append(soup.find_all(class_='tableText-01'))


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
