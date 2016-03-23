from selenium import webdriver


browser = webdriver.Chrome(executable_path = '../../dependencies/chromedriver')
browser.get('https://emaryland.buyspeed.com/bso/external/publicBids.sdo')

MDNumContracts = browser.find_element_by_xpath("/html/body/form/table[4]/tbody/tr[4]/td/table/tbody/tr[1]/td")
MDNumContracts = MDNumContracts.get_attribute('innerHTML')
MDNumContracts = str(MDNumContracts).rsplit(' ', 1)[1]
print MDNumContracts

# for i in range(30):	
# 	a = browser.execute_script("viewPage(" + str(i) + ")")
# 	print a

