from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.zhuce_page import ZhuPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def homepage(self):
        return HomePage(self.driver)

    @property
    def zhucepage(self):
        return ZhuPage(self.driver)


    @property
    def loginpage(self):
        return LoginPage(self.driver)

    @property
    def mepage(self):
        return MePage(self.driver)

