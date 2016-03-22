from selenium import webdriver
import os


'''Initial Setup for Scraping MD State Contracts'''
path_to_chromedriver = '/home/david/Projects/cvore/dependencies/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://emaryland.buyspeed.com/bso/external/publicBids.sdo'
browser.get(url)
'''Initial Setup for Scraping MD State Contracts'''


for index in range(14): #!!! HOW DO WE TELL THIS TO END WHEN THERE ARE NO MORE NEW PAGES
	try:
		temp = browser.find_element_by_xpath("/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[" + str(index) + "]").click()
		#!!!SAVE TO FILE OR BS4 OR BOTH?
		browser.forward()
	except:
		pass



# temp = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[12]').click() #Find the link to the second page of contracts and click on it
# browser.forward() #Moves the object in browser to where the newly opened page is




# print browser.page_source #Used to test where the current browser object is

# '''DOWNLOAD FILE NOT WORKING'''
# results_url = browser.find_element_by_xpath('/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[2]/td/a[1]').get_attribute('href')
# os.system('wget {}'.format(results_url))
# '''DOWNLOAD FILE NOT WORKING'''
