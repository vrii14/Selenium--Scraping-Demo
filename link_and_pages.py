
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "D:\selenium\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.coep.org.in/")

main_window = driver.current_window_handle

link = driver.find_element_by_link_text("NOTICES")
link.click()


try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "OOT T-II Time Table for Common Theory Courses"))
    )
    element.click()
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "OOT T-II Time Table for Common Theory Courses"))
    )
    element.click()

    time.sleep(10)

    driver.switch_to_window(main_window)
    time.sleep(3)
    driver.back()
    time.sleep(3)
finally:
    driver.quit()