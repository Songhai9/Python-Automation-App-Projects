# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL
URL = 'https://orteil.dashnet.org/experiments/cookie/'

# Configuring webdriver and buttons
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
cookie_button = driver.find_element(By.ID, value="cookie")
store = driver.find_element(By.ID, value="store")
money = driver.find_element(By.ID, value="money")
ratio = driver.find_element(By.ID, value="cps")

# Time settings
inter = 0.001
inter2 = 5
time_since_started = 0
temps_debut = time.time()

# Buttons
# Cursor
cursor_btn = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b")
value_cursor = int(cursor_btn.text.split('-')[1].replace(',', ''))
# Grandma
grandma_btn = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
value_grandma = int(grandma_btn.text.split('-')[1].replace(',', ''))
# Factory
factory_btn = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b")
value_factory = int(factory_btn.text.split('-')[1].replace(',', ''))
# Mine
mine_btn = driver.find_element(By.CSS_SELECTOR, value="#buyMine b")
value_mine = int(mine_btn.text.split('-')[1].replace(',', ''))
# Shipment
shipment_btn = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b")
value_shipment = int(shipment_btn.text.split('-')[1].replace(',', ''))
# Alchemy Lab
alchemy_btn = driver.find_element(By.CSS_SELECTOR, value="#buyAlchemy\\ lab b")
value_alchemy = int(alchemy_btn.text.split('-')[1].replace(',', ''))

# Portal
portal_btn = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")
value_portal = int(portal_btn.text.split('-')[1].replace(',', ''))


def check_booster(available):
    if available < 15:
        return
    if value_cursor <= available < value_grandma:
        return "buyCursor"
    elif value_grandma <= available < value_factory:
        return "buyGrandma"
    elif value_factory <= available < value_mine:
        return "buyFactory"
    elif value_mine <= available < value_shipment:
        return "buyMine"
    elif value_shipment <= available < value_alchemy:
        return "buyShipment"
    elif value_alchemy <= available < value_portal:
        return "buyAlchemy lab"
    else:
        return "buyPortal"


count = 0

while time.time() - temps_debut < 120:
    cookie_button.click()
    time.sleep(inter)
    time_since_started += inter

    if (time.time() - temps_debut) % inter2 < 0.1:
        btn = driver.find_element(By.ID, value=check_booster(int(money.text.replace(',', ''))))
        btn.click()

print(ratio.text)
driver.quit()
