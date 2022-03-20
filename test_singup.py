import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Testphptravels_singup(unittest.TestCase):
    website_url = 'https://www.phptravels.net/signup'
    send_firstname = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[1]/div/input'
    send_textfirst = 'San'
    send_lastname = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[2]/div/input'
    send_textlast = 'Gem'
    phone_by_xpath = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[3]/div/input'
    send_phone = '+447950636683'
    mail_by_xpath = '/html/body/div[1]/div/div[2]/div[2]/div/form/div[4]/div/input'
    send_mail = 'nijefo8339@shopxda.com'
    password_by_xpath = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[5]/div/input'
    send_password = '447950636683'
    sing_up_button = '//*[@id="fadein"]/div[1]/div/div[2]/div[2]/div/form/div[7]/button'

    def setUp(self):
        print('Test started')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.website_url)

    def test_signup(self):
        time.sleep(2)
        driver = self.driver
        action = ActionChains(driver)
        send_singup1 = driver.find_element(By.XPATH, self.send_firstname)
        send_singup1.send_keys(self.send_textfirst)
        time.sleep(2)
        send_singup2 = driver.find_element(By.XPATH, self.send_lastname)
        send_singup2.send_keys(self.send_textlast)
        time.sleep(2)
        phone_inp = driver.find_element(By.XPATH, self.phone_by_xpath)
        phone_inp.send_keys(self.send_phone)
        time.sleep(2)
        mail_inp = driver.find_element(By.XPATH, self.mail_by_xpath)
        mail_inp.send_keys(self.send_mail)
        time.sleep(2)
        password_inp = driver.find_element(By.XPATH, self.password_by_xpath)
        password_inp.send_keys(self.send_password)
        time.sleep(2)
        sing_up_btn = driver.find_element(By.XPATH, self.sing_up_button)
        action.move_to_element(sing_up_btn).click()
        time.sleep(2)

    def tearDown(self):
        print('Test finished')
        driver = self.driver
        driver.quit()


if __name__ == '__main__':
    unittest.main()
