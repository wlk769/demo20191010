from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    username = By.ID,"com.yunmall.lc:id/logon_account_textview"
    password = By.ID,"com.yunmall.lc:id/logon_password_textview"
    button = By.ID,"com.yunmall.lc:id/logon_button"


    def  input_username(self,text):
        self.input(self.username,text)

    def input_password(self,text):
        self.input(self.password,text)

    def click_button(self):
        self.click(self.button)





