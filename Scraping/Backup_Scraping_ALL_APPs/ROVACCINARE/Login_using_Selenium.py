import time
# importing webdriver from selenium
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
webdriver_path = r'C:/Users/Horace.000/AppData/Local/Programs/Python/Python38/EdgeDriverServer/msedgedriver_win64.exe'
browser = webdriver.Edge(webdriver_path) 
 
# URL of website
url = "https://programare.vaccinare-covid.gov.ro/auth/login#/user/profile"
 
# Opening the website
browser.get(url)


# The browser will get maximized
browser.maximize_window()

username = browser.find_element_by_id("mat-input-0")
username.clear()
username.send_keys("cristadoina@gmail.com")

password = browser.find_element_by_id("mat-input-1")
password.clear()
password.send_keys("Doina05$")

time.sleep(5)

#wait = WebDriverWait(browser, 20)

#try:
#    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME 'mat-button-wrapper')))
#finally:
#    browser.quit()

# getting the button by class name
button_Autentificare = browser.find_element_by_class_name('mat-button-wrapper')
 
# clicking on the button
button_Autentificare.click()

#try:
#    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "nav-link-title")))
#finally:
#    browser.quit()

time.sleep(5)

#button_Beneficiari = browser.find_element_by_class_name('nav-link-title')
#button_Beneficiari.click()
