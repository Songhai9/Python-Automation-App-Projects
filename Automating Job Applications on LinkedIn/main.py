# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
from selenium.common.exceptions import NoSuchElementException

# Getting environment variables
load_dotenv()
linkedin_username = os.getenv('LINKEDIN_USERNAME')
linked_password = os.getenv('LINKEDIN_PASSWORD')
phone_number = os.getenv('PHONE_NUMBER')

# Configuring the driver and getting the webpage
URL = 'https://www.linkedin.com/jobs/search/?currentJobId=4121100623&f_AL=true&geoId=105015875&keywords=Préparateur%20de%20commande&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Logging in
sign_in_btn = driver.find_element(By.CSS_SELECTOR, value="button[data-modal='base-sign-in-modal']")
sign_in_btn.click()
time.sleep(3)
username_field = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
username_field.send_keys(linkedin_username)
password_field = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(linked_password)
login_btn = driver.find_element(By.XPATH,
                                value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
login_btn.click()

# Apply for all the jobs
time.sleep(3)
job_list = driver.find_elements(By.CLASS_NAME, value="artdeco-entity-lockup__content")
for job in job_list:
    job.click()
    try:
        apply = driver.find_element(By.CSS_SELECTOR,
                                    value="[data-live-test-job-apply-button]")
    except NoSuchElementException:
        print('Probably already applied, skipping to the next job. . .')
        continue
        
    apply.click()
    time.sleep(5)
    phone_field = driver.find_element(By.ID,
                                      value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4133399651-12901104562-phoneNumber-nationalNumber")
    phone_value = phone_field.get_attribute("value")
    if not phone_value:
        phone_field.send_keys(phone_number)

    try:
        send_apply = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Envoyer la candidature]")
        send_apply.click()
    except NoSuchElementException:
        print('multiple step necessary, skipping to the next job')
        exit_application = driver.find_element(By.CSS_SELECTOR, value="[aria-label='Ignorer']")
        exit_application.click()
        suppress = driver.find_element(By.CSS_SELECTOR, value="[data-test-dialog-secondary-btn]")
        suppress.click()
