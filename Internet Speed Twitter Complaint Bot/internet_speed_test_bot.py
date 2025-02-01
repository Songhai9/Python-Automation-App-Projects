import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv

SPEEDTEST_URL = "https://www.speedtest.net"
TWITTER_URL = "https://x.com/"

load_dotenv()

twitter_email = os.getenv("TWITTER_EMAIL")
twitter_password = os.getenv("TWITTER_PASSWORD")
twitter_username = os.getenv("TWITTER_USERNAME")


class InternetSpeedTestBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # Get to the webpage
        self.driver.get(SPEEDTEST_URL)

        # Rejecting cookies
        reject_btn = self.driver.find_element(
            By.ID, value="onetrust-reject-all-handler"
        )
        reject_btn.click()

        # Starting the speedtest
        go_btn = self.driver.find_element(By.CLASS_NAME, value="js-start-test")
        go_btn.click()
        time.sleep(50)

        # Ignorign ad
        back_to_results_btn = self.driver.find_element(
            By.LINK_TEXT, value="Back to test results"
        )
        back_to_results_btn.click()

        # Storing and printing values
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        print(f"upload speed = {self.up}, {self.down}")

    def tweet_at_provider(self):
        # Twitter webpage
        self.driver.get(TWITTER_URL)

        # Logging in
        time.sleep(5)
        sign_in_btn = self.driver.find_element(
            By.XPATH,
            value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[3]/a/div',
        )

        # Rejecting cookies
        refuse_cookie_btn = self.driver.find_element(
            By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/button[2]/div'
        )
        refuse_cookie_btn.click()

        # Sign in
        sign_in_btn.click()
        time.sleep(3)
        username_input = self.driver.find_element(
            By.CSS_SELECTOR,
            value='input[autocapitalize="sentences"][autocomplete="username"][name="text"]',
        )
        username_input.click()
        username_input.send_keys(twitter_email)
        next_btn = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div',
        )
        next_btn.click()

        # Twitter may ask for the username if suspicious activity has been detected
        time.sleep(3)
        self.driver.switch_to.active_element.send_keys(twitter_username)
        next_btn2 = self.driver.find_element(
            By.CSS_SELECTOR,
            value=".css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l",
        )
        next_btn2.click()

        # Password & login
        time.sleep(2)
        password_input = self.driver.find_element(By.NAME, value="password")
        password_input.send_keys(twitter_password)
        login_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            value=".css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-19yznuf.r-64el8z.r-1fkl15p.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l",
        )
        login_btn.click()
        time.sleep(5)

        # Writing and sending the tweet
        tweet_input = self.driver.find_element(
            By.CSS_SELECTOR,
            value=".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr",
        )

        # We may first check for conditions before sending the tweet (if the upload/download speed is under a certain value
        tweet_input.send_keys(
            f"@tdsxom ton code marche bien: valeur upload = {self.up}, valeur download = {self.down}"
        )
        send_twt_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            value=".css-175oi2r.r-sdzlij.r-1phboty.r-rs99b7.r-lrvibr.r-1cwvpvk.r-2yi16.r-1qi8awa.r-3pj75a.r-1loqt21.r-o7ynqc.r-6416eg.r-1ny4l3l",
        )
        send_twt_btn.click()
