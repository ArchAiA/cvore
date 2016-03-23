import datetime
from selenium import webdriver




class ScrapeMD(object):
# url = 'http://emaryland.buyspeed.com/bso/external/publicBids.sdo'
	# self.url = extra

	def __init__(self, url, browser):
		self.url = url
		self.browser = browser
		self.browser.get(self.url)
		# self.IterateThroughMDPages()

	def SaveToFile(self, scraped_data, index):
		to_be_written = scraped_data.encode('utf8')

		f = open("../htmloutput/MD/MDPage" + str(index) + "-" + str(datetime.datetime.now()) + ".html", 'w')
		f.write(to_be_written)
		f.close()


	def IterateThroughMDPages(self):
		for index in range(14): #!!! HOW DO WE TELL THIS TO END WHEN THERE ARE NO MORE NEW PAGES
			try:
				self.SaveToFile(self.browser.page_source, index)								
				self.browser.find_element_by_xpath("/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[" + str(index) + "]").click()
				self.browser.forward()
			except:
				pass






# temp = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[12]').click() #Find the link to the second page of contracts and click on it
# browser.forward() #Moves the object in browser to where the newly opened page is




# print browser.page_source #Used to test where the current browser object is

# '''DOWNLOAD FILE NOT WORKING'''
# results_url = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[1]').get_attribute('href')
# os.system('wget {}'.format(results_url))
# '''DOWNLOAD FILE NOT WORKING'''
