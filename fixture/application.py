from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver=WebDriver()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)


    def open_home_page(self):
        driver=self.driver
        driver.get("http://localhost:8080/addressbook")

    def destroy(self):
        self.driver.quit()