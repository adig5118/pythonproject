import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome()
d.maximize_window()

d.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")

#enter the text in text box

text_field = d.find_element(By.NAME, 'username')
text_field.send_keys("Simhadri")
text_field.send_keys(Keys.ENTER)
time.sleep(10)







