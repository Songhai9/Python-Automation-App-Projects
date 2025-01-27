from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = 'https://secure-retreat-92358.herokuapp.com'
driver.get(URL)

first_name = driver.find_element(By.NAME, value='fName')
first_name.send_keys('Oumarou')

last_name = driver.find_element(By.NAME, value='lName')
last_name.send_keys('Maiga')

email = driver.find_element(By.NAME, value='email')
email.send_keys('doosix@outlook.fr')

signup_btn = driver.find_element(By.CSS_SELECTOR, value='[type="submit"]')
signup_btn.click()
