import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Utilities_testing_phptravels import login
from Utilities_testing_phptravels import hotels


class Testphptravels_search_hotels(unittest.TestCase):
    website_url = 'https://www.phptravels.net/login'
    search = '//*[@id="select2-hotels_city-container"]'
    search_field = '//*[@id="fadein"]/span/span/span[1]/input'
    search_text = 'Yerevan'
    yerevan_am = '//*[@id="select2-hotels_city-results"]/li'
    search_btn = '//*[@id="submit"]'

    def setUp(self):
        print('Test started')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website_url)

    def test_searching(self):
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
        search1 = driver.find_element(By.XPATH, self.search)
        action.move_to_element(search1).click().perform()
        time.sleep(4)
        send_text = driver.find_element(By.XPATH, self.search_field)
        send_text.send_keys(self.search_text)
        time.sleep(4)
        click_yerevan = driver.find_element(By.XPATH, self.yerevan_am)
        action.move_to_element(click_yerevan).click().perform()
        click_search = driver.find_element(By.XPATH, self.search_btn)
        action.move_to_element(click_search).click().perform()
        time.sleep(4)

    def tearDown(self):
        print('Test finished')
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
