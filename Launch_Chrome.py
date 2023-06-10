import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome()
d.maximize_window()
d.get("https://google.com/")
search_elem = d.find_element(By.NAME, 'q')
search_elem.send_keys("Amazon.in")
search_elem.send_keys(Keys.ENTER)
amazon_link = d.find_element(By.XPATH, "//span[@class = 'OSrXXb VN4UC']")
amazon_link.click()

# Search product in Amazon
#search_product = d.find_element(By.XPATH, "//input[@id = 'twotabsearchtextbox']")
search_product = d.find_element(By.ID, "twotabsearchtextbox")
search_product.send_keys("Nothing Mobile")
search_product.send_keys(Keys.ENTER)
time.sleep(10)