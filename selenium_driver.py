import time
from selenium import webdriver

driver = webdriver.Chrome("C:/Pyautomators/drivers/chromedriver.exe")
driver.get("https://google.com.br")
print(driver.title)
time.sleep(8)
driver.quit()
