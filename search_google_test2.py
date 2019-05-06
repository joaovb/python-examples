from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

browser = webdriver.Chrome(executable_path=r'C:\Pyautomators\drivers\chromedriver.exe')
browser.get('http://www.google.com')

q = driver.find_element(By.NAME, 'q')
q.send_keys('webdriver')
q.submit()

#print driver.title