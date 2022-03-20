import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Utilities_testing_phptravels import login
from Utilities_testing_phptravels import hotels
from Utilities_testing_phptravels import search
from Utilities_testing_phptravels import details


class Testphptravels_select(unittest.TestCase):
    website_url = 'https://www.phptravels.net/login'
    click_on = '//*[@id="SearchBoxContainer"]/div/div/div[4]'
    select = '//*[@id="contentContainer"]/div[3]/ol/li[2]/div/a/div[1]/div[3]/div/div[3]/button/div/div/div/div/svg'

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
        self.driver.find_element(By.XPATH, search.search).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, search.search_field).send_keys(search.search_text)
        time.sleep(4)
        self.driver.find_element(By.XPATH, search.yerevan_am).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, search.search_btn).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, details.details).click()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(4)
        click = driver.find_element(By.XPATH, self.click_on)
        action.move_to_element(click).click().perform()
        time.sleep(4)
        select_room = driver.find_element(By.XPATH, self.select)
        action.move_to_element(select_room).click().perform()
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(4)

    def tearDown(self):
        print('Test finished')
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
