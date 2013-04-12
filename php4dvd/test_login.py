from selenium import webdriver
from selenium.common.exceptions import *
import unittest


class Untitled(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(
            capabilities={'native_events': False})
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
