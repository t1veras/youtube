#Thiago Veras 05/04/2023

#sudo apt --fix-broken install

#sudo apt install python3
#sudo apt install python3-pip
#pip3 install selenium
#pip3 install webdriver_manager

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

class Link():

	def linkh(self):
		
		try:
			links = []
			driver.get("https://www.google.com/")
			time.sleep(10)
			elements = driver.find_elements(by=By.TAG_NAME, value="a")
			for elem in elements:
				href = elem.get_attribute("href")
				links.append(href)
			print(links)
			
		except Exception as ex:
			print(ex)

bot = Link()
bot.linkh()