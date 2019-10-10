from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ZhuPage(BaseAction):

    btn_ok_me = By.ID,"com.yunmall.lc:id/textView1"

    def click_btn_ok_me(self):
        self.click(self.btn_ok_me)