import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Utilities_testing_phptravels import login
from Utilities_testing_phptravels import hotels
from Utilities_testing_phptravels import search
from Utilities_testing_phptravels import details
from Utilities_testing_phptravels import select
from Utilities_testing_phptravels import booking

class Testphptravels_filling(unittest.TestCase):
    website_url = 'https://www.phptravels.net/login'
    full_name_xpath = '//*[@id="firstName_lastName"]'
    full_name_text = 'San Gem'
    email_xpath = '//*[@id="email"]'
    retype_mail_xpath = '//*[@id="retypeEmail"]'
    number_xpath = '//*[@id="phoneNumber"]'
    next_xpath = '//*[@id="SiteContent"]/div/div[1]/div[5]/div/button/div/div/span'

    def setUp(self):
        print('Test started')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website_url)

    def test_filling(self):
        time.sleep(2)
        driver = self.driver
        action = ActionChains(driver)
        time.sleep(2)
        self.driver.find_element(By.XPATH, login.send_email).send_keys(login.send_text_email)
        time.sleep(2)
        self.driver.find_element(By.XPATH, login.send_password).send_keys(login.send_text_password)
        time.sleep(2)
        self.driver.find_element(By.XPATH, login.login_button).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, hotels.click_hotels).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, search.search).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, search.search_field).send_keys(search.search_text)
        time.sleep(2)
        self.driver.find_element(By.XPATH, search.yerevan_am).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, search.search_btn).click()
        time.sleep(6)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(4)
        self.driver.find_element(By.XPATH, details.detail).click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(4)
        self.driver.find_element(By.XPATH, select.click_on_box).click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(4)
        self.driver.find_element(By.XPATH, select.select_room).click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(4)
        self.driver.find_element(By.XPATH, booking.deal).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, booking.book_now).click()
        time.sleep(4)
        full = driver.find_element(By.XPATH, self.full_name_xpath)
        full.send_keys(self.full_name_text)
        time.sleep(4)
        email = driver.find_element(By.XPATH, self.email_xpath)
        email.send_keys(login.send_text_email)
        time.sleep(4)
        retype_email = driver.find_element(By.XPATH, self.retype_mail_xpath)
        retype_email.send_keys(login.send_text_email)
        time.sleep(4)
        number = driver.find_element(By.XPATH, self.number_xpath)
        number.send_keys(login.numbers)
        time.sleep(4)

    def tearDown(self):
        print('Test finished')
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
