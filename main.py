from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)

PROMISED_DOWN = 100
PROMISED_UP = 50

TWITTER_MAIL = #your email
PASS = #your password


class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        driver.get(url="https://www.speedtest.net/")
        time.sleep(5)
        start_button = driver.find_element(By.CLASS_NAME,value="start-text")
        start_button.click()
        time.sleep(50)
        self.down = float(driver.find_element(By.CLASS_NAME,value="download-speed").text)
        self.up = float(driver.find_element(By.CLASS_NAME,value="upload-speed").text)




    def tweet_at_provider(self):
        driver.get(url="https://x.com/i/flow/login")
        time.sleep(5)
        box = driver.find_element(By.CLASS_NAME,value="r-fdjqy7")
        box.send_keys(TWITTER_MAIL,Keys.ENTER)
        time.sleep(5)
        passbox = driver.find_element(By.NAME,value="password")
        passbox.send_keys(PASS,Keys.ENTER)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH,
                                                value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()



bot = InternetSpeedTwitterBot(driver)
bot.get_internet_speed()


if bot.down<PROMISED_DOWN or bot.up < PROMISED_UP:

    bot.tweet_at_provider()
