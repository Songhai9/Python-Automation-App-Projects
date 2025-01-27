from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver.get(URL)
editor_count = driver.find_elements(By.CSS_SELECTOR, value="[title='Special:Statistics']")
print(editor_count[0].text)
editor_count[0].click()

# driver.quit()
