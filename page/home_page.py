from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):


    me_btn = By.ID,"com.yunmall.lc:id/tab_me"


    def click_me_btn(self):
        self.click(self.me_btn)


    def login_if_not(self,page):
        self.click_me_btn()
        if self.driver.current_activity != 'com.yunmall.ymctoc.ui.activity':
            return

        page.zhucepage.click_btn_ok_me()
        page.loginpage.input_username('itheima_test')
        page.loginpage.input_password('itheima')
        page.loginpage.click_button()



