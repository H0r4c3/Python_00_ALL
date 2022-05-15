'https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python'

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver_path_64 = r'C:/Users/Horace.000/AppData/Local/Programs/Python/Python310/EdgeDriverServer/msedgedriver_win64.exe'
driver = webdriver.Edge(webdriver_path_64)

driver.get('https://bing.com')

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('WebDriver')
element.submit()

time.sleep(5)
driver.quit()