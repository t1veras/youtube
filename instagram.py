#Thiago Veras 05/04/2023

#https://www.instagram.com/

#sudo apt --fix-broken install

#sudo apt install python3
#sudo apt install python3-pip
#pip3 install selenium
#pip3 install webdriver_manager

#t1veras.backup
#NjdVXP6n7.J8!<c

import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# username, password, profile
bot_username = 't1veras.backup'
bot_password = 'NjdVXP6n7.J8!<c'
profiles = ['test_debugbm']

class Instagram():

	def __init__(self, username, password):
		self.username = username
		self.password = password
		options = Options()
		options.add_experimental_option("excludeSwitches", ["enable-logging"])

	def login(self):
		try:
			driver.get('https://www.instagram.com')
			time.sleep(random.randrange(3, 5))
			username_input = driver.find_element(by=By.NAME, value="username")
			username_input.clear()
			username_input.send_keys(self.username)
			time.sleep(random.randrange(2, 4))
			password_input = driver.find_element(by=By.NAME, value="password")
			password_input.clear()
			password_input.send_keys(self.password)
			time.sleep(random.randrange(1, 2))
			password_input.send_keys(Keys.ENTER)
			time.sleep(random.randrange(3, 5))
		except Exception as ex:
			print(ex)

	def get_followers(self, users):
		followers_list = []
		for user in users:
			driver.get('https://instagram.com/' + user)
			time.sleep(random.randrange(3, 5))
			# F12 -> copy full xpath
			try:
				driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/ul/li[2]/button/div/span")
				followers_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/ul/li[2]/button/div/span")
				time.sleep(3)
			except:
				 followers_button = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/span")
			count = followers_button.get_attribute('title')
			if '.' in count:
				count = int(''.join(count.split('.')))
			else:
				count = int(count)
			followers_button.click()
			loops_count = int(count / 12)
			time.sleep(random.randrange(8,10))
			followers_a = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
			time.sleep(random.randrange(5,7))
			
			try:		
				for i in range(1, loops_count + 1):
					driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_a)
					time.sleep(random.randrange(8, 10))
					for elem in followers_a.find_elements(by=By.TAG_NAME, value="a"):
						elem = elem.get_attribute("href")
						elemr = elem.replace("https://www.instagram.com/", "")
						elem = elemr.replace("/", "")
						followers_list.append(elem)
					time.sleep(1)
					f3 = open('followers.txt', 'w')
					for list in followers_list:
						f3.write(list + '\n')
				time.sleep(random.randrange(3, 5))
			except Exception as ex:
				print(ex)

		return followers_list

	def cut(self):
		try:
			seen = set()
			with open('followers.txt', 'r') as fin, open('followers-unique.txt', 'w') as fout:
    				for line in fin:
        				h = hash(line)
        				if h not in seen:
            					fout.write(line)
            					seen.add(h)
			os.remove("followers.txt")
		except Exception as ex:
			print(ex)

bot = Instagram(bot_username, bot_password)
bot.login()
time.sleep(3)
followers = bot.get_followers(profiles)
bot.cut()