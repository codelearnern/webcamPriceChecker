# from bs4 import BeautifulSoup
# import requests

# webpage = requests.get("https://www.amazon.com/Logitech-C920x-Pro-HD-Webcam/dp/B085TFF7M1/ref=sr_1_4")

# print(webpage.content)
# soup = BeautifulSoup(webpage.content, "html.parser")

# price = soup.find(id="priceblock_ourprice")

# print(price.prettify())

# NOT WORKING DUE TO AMAZON BLOCKING BEAUTIFULSSOUP BOTS

from selenium import webdriver
from sendGmail.sender import send_msg, create_msg
from sendGmail.serviceStuff import Create_Service
import time

CLIENT_SECRET_FILE = 'sendGmail/credentials.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe", options=options)
while True:
	driver.get("https://www.amazon.com/Logitech-C920x-Pro-HD-Webcam/dp/B085TFF7M1/ref=sr_1_4")
	time.sleep(3)
	c920xPrice = driver.find_element_by_id("priceblock_ourprice")

	if float(c920xPrice.text.replace("$", "")) < 67.5:
		msg = create_msg("ayaan.panda1@gmail.com",
						"ayaan.panda1@gmail.com",
						"LOGITECH c920",
						f"""LOGITECH C920 IS LESS THAN $67.50 DOLLARS, it is {c920xPrice.text} 
						GO TO AMAZON AND BUY IT NOW PLEASE 
						,by the way, this is from a bot you created :)""")
		send_msg(service, "ayaan.panda1@gmail.com", msg)
	else:
		print("it is more than $67.50 dollars, don't buy it")

	time.sleep(1000)