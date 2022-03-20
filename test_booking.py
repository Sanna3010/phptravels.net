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


class Testphptravels_booking(unittest.TestCase):
    website_url = 'https://www.phptravels.net/login'
    book_now = '//*[@id="ChildRoom-CqcBCP6Ul6wDEAIgAjAGSg0zNjVEMTAwUF8xMDBQUIq2A3qFAVNvbWUoNzE0NDk4OTkpfDQ0ODk4MDI4N3wxfDIwMTgxNDQ0Ml8yMDkyNTMzNDZAbnwzfFJPfExpc3QoKXwzNjVEMTAwUF8xMDBQfFNvbWUoMXxST3w3MTQ0OTg5OXx4aXdhbnwyMDE4MTQ0NDJfMjA5MjUzMzQ2QG58MjAxODE0NDQyfCkSAggBGgQoBjAB"]/div/div[5]/div[1]/div/div[1]/button'
    deal = '//*[@id="hotelNavBar"]/div/div/div/div/button'
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
        dealn = driver.find_element(By.XPATH, self.deal)
        action.move_to_element(dealn).click().perform()
        time.sleep(4)
        booking = driver.find_element(By.XPATH, self.book_now)
        action.move_to_element(booking).click().perform()
        time.sleep(4)


    def tearDown(self):
        print('Test finished')
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
