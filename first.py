
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='C:\Python27\chromedriver.exe')
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys("Surgical strike 2")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(8) # sleep for 5 seconds so you can see the results
browser.quit()