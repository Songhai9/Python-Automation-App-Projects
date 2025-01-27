from selenium import webdriver
from selenium.webdriver.common.by import By
import json

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
URL = 'https://www.python.org'
driver.get(URL)

upcoming_events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div')

upcoming_events_text = upcoming_events.text
list_of_events = upcoming_events_text.split('\n')
list_of_events = list_of_events[2:]
print(list_of_events)

event_dict = {i: {'time': list_of_events[2 * i], 'name': list_of_events[(2 * i) + 1]} for i in
              range(len(list_of_events) // 2)}

event_dict_formatted = json.dumps(event_dict, indent=4)
print(event_dict_formatted)
driver.quit()
