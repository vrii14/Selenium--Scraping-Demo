
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "D:\selenium\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.coep.org.in/")

search = driver.find_element_by_id("edit-search-block-form--2")
search.send_keys("computer")
search.send_keys(Keys.RETURN)

time.sleep(5)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "block-system-main"))
    )

    articles = main.find_elements_by_tag_name("li")
    for article in articles:
    	header = article.find_element_by_class_name("title")
    	print(header.text)

finally:
    driver.quit()
