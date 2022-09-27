from selenium import webdriver
from Pages.CardsPage import SearchHelper


class App:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/bin/chromedriver.exe")
        self.search = SearchHelper(self)

    def site_open(self):
        self.driver.get("http://HR:test@qa.digift.ru/")
        self.driver.maximize_window()

    def session_kill(self):
        self.driver.quit()
