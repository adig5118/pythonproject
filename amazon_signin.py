import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

d = webdriver.Chrome()
d.maximize_window()

d.get(" https://google.com/")

search_elem = d.find_element(By.NAME, 'q')
search_elem.send_keys("amazon.in")
search_elem.send_keys(Keys.RETURN)

amazon_link = d.find_element(By.XPATH, "//span[@class = 'OSrXXb VN4UC']")
amazon_link.click()
time.sleep(10)

# Signin panel
signin_panel = d.find_element(By.CLASS_NAME, 'nav-line-2')
ActionChains = ActionChains(d)
ActionChains.click(signin_panel)
ActionChains.move_to_element(signin_panel)
ActionChains.perform()


