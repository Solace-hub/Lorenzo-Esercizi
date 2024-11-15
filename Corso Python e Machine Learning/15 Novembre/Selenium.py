import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time




options = Options()
options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

driver.get("https://www.wikipedia.org/")

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "searchInput"))
)

search_box.send_keys("Python (programming language)" + Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.title_contains("Python (programming language)")
)

print(driver.title)

driver.quit()












'''driver = webdriver.Firefox()
time.sleep(5)
driver.get("https://www.wikipedia.org/")
search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Python (programming language)" + Keys.RETURN)
time.sleep(5)
print("Titolo della pagina:", driver.title)
driver.quit()'''