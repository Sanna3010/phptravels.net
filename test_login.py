import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Testphptravels_login(unittest.TestCase):
    website_url = 'https://www.phptravels.net/login'
    send_email = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input'
    send_text_email = 'nijefo8339@shopxda.com'
    send_password = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/input'
    send_text_password = '447950636683'
    login_button = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/button'

    def setUp(self):
        print('Test started')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website_url)

    def test_login(self):
        time.sleep(2)
        driver = self.driver
        action = ActionChains(driver)
        send_mail = driver.find_element(By.XPATH, self.send_email)
        send_mail.send_keys(self.send_text_email)
        time.sleep(2)
        send_passwords = driver.find_element(By.XPATH, self.send_password)
        send_passwords.send_keys(self.send_text_password)
        time.sleep(2)
        login_btn = driver.find_element(By.XPATH, self.login_button)
        action.move_to_element(login_btn).click().perform()
        time.sleep(2)

    def tearDown(self):
        print('Test finished')
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
