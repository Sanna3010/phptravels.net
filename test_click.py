import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Utilities_testing_phptravels import login


class Testphptravels_click_hotels(unittest.TestCase):
    website_url = 'https://www.phptravels.net/login'
    click_hotels = '//*[@id="fadein"]/header/div[2]/div/div/div/div/div[2]/nav/ul/li[2]/a'

    def setUp(self):
        print('Test started')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website_url)

    def test_clicking(self):
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
        click = driver.find_element(By.XPATH, self.click_hotels)
        action.move_to_element(click).click().perform()
        time.sleep(2)

    def tearDown(self):
        print('Test finished')
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
