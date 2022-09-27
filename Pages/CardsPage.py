from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SearchHelper:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

    # def login_alert(self):
    #     self.obj = self.driver.switch_to.alert
    #     self.obj.send_keys("HR")
    #     self.obj.send_keys(Keys.TAB)
    #     self.obj.send_keys("test")
    #     self.obj.send_keys(Keys.ENTER)

    def card_500_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "*[class=\"js-par-option par-options__item\"][data-value=\"500\"]>button")

    def card_1000_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "*[class=\"js-par-option par-options__item\"][data-value=\"1000\"]>button")

    def card_2000_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "*[class=\"js-par-option par-options__item\"][data-value=\"2000\"]>button")

    def card_3000_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "*[class=\"js-par-option par-options__item\"][data-value=\"3000\"]>button")

    def card_5000_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "*[class=\"js-par-option par-options__item\"][data-value=\"5000\"]>button")

    def card_10000_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "*[class=\"js-par-option par-options__item\"][data-value=\"10000\"]>button")

    def card_value_input(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(By.CSS_SELECTOR,
                                        "*[id=\"range-value-input\"]")