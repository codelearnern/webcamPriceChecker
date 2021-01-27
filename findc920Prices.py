from selenium import webdriver
import time

def c920xPrice():
	driver_options = webdriver.ChromeOptions()
	driver_options.add_argument('headless')

	driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe", options=driver_options)
	driver.maximize_window()
	driver.get("https://www.amazon.com/Logitech-C920x-Pro-HD-Webcam/dp/B085TFF7M1/ref=sr_1_3")

	time.sleep(2)

	price = driver.find_element_by_id("priceblock_ourprice").text
	return price

def c920Price():
	driver_options = webdriver.ChromeOptions()
	driver_options.add_argument('headless')

	driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe", options=driver_options)
	driver.maximize_window()

	driver.get("https://www.amazon.com/Logitech-Widescreen-Calling-Recording-Desktop/dp/B006JH8T3S/ref=sr_1_4")

	time.sleep(2)

	price = driver.find_element_by_css_selector("#aod-price-1 > span > span.a-offscreen").text
	return price