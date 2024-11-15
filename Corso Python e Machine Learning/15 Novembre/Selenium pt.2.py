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

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys("student") 
password_field.send_keys("Password123")

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

time.sleep(5)

page_text = driver.page_source
print(page_text)

logout_button =  driver.find_element(By.LINK_TEXT, "Log out")
logout_button.click()

print(driver.title)
driver.quit()