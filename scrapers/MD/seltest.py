import datetime
from selenium import webdriver




class ScrapeMD(object):
# url = 'http://emaryland.buyspeed.com/bso/external/publicBids.sdo'
	# self.url = extra

	def __init__(self, url, browser):
		self.url = url
		self.browser = browser
		self.browser.get(self.url)
		self.numberOfContracts = self.GetNumberOfContracts()
		print self.numberOfContracts
		# self.IterateThroughMDPages()

	def SaveToFile(self, scraped_data, index):
		to_be_written = scraped_data.encode('utf8')

		f = open("../htmloutput/MD/MDPage" + str(index) + "-" + str(datetime.datetime.now()) + ".html", 'w')
		f.write(to_be_written)
		f.close()


	def IterateThroughMDPages(self):
		numberOfPages = self.numberOfContracts / 25
		print numberOfPages
		for index in range(1,numberOfPages+2): #Why do I have to add the +2 to the number of pages to cover all of the pages.  I would understand +1, but wtf is up with +2
			try:
				# self.browser.find_element_by_xpath("/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[" + str(index) + "]").click()
				self.browser.execute_script("viewPage(" + str(index) + ")")
				self.browser.forward()
				self.SaveToFile(self.browser.page_source, index)												
			except:
				pass

	def GetNumberOfContracts(self):
		MDNumContracts = self.browser.find_element_by_xpath("/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[1]/td")
		MDNumContracts = MDNumContracts.get_attribute('innerHTML')
		MDNumContracts = str(MDNumContracts).rsplit(' ', 1)[1]
		return int(MDNumContracts)






# temp = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[12]').click() #Find the link to the second page of contracts and click on it
# browser.forward() #Moves the object in browser to where the newly opened page is




# print browser.page_source #Used to test where the current browser object is

# '''DOWNLOAD FILE NOT WORKING'''
# results_url = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[1]').get_attribute('href')
# os.system('wget {}'.format(results_url))
# '''DOWNLOAD FILE NOT WORKING'''
