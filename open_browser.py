from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie('C:\drivers-selenium\IEDriverServer.exe')
driver= webdriver.Chrome(executable_path=r'C:\drivers-selenium\chromedriver.exe') #drive chrome
#driver = webdriver.Firefox(executable_path=r'C:\Pyautomators\drivers\geckodriver.exe') #driver firefox
driver.get("https://www.google.com.br")
assert "Google" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()
