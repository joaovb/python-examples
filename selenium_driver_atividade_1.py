import time
from selenium import webdriver

driver = webdriver.Chrome("drivers\chromedriver.exe")
driver.get("https://google.com.br") #abre página do google
print(driver.title)
time.sleep(8)
driver.quit()
