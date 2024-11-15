import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3)

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
time.sleep(3)


username_field.send_keys("student") 
password_field.send_keys("Password123")
time.sleep(3)

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()
time.sleep(3)

page_text = driver.page_source
print(page_text)
time.sleep(3)

logout_button =  driver.find_element(By.LINK_TEXT, "Log out")
logout_button.click()
time.sleep(3)

print(driver.title)
driver.quit()