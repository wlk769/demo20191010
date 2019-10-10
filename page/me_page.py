from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    get_me_page = By.ID,"com.yunmall.lc:id/tv_user_nikename"


    def get_me_page_me(self):
        return self.find_element(self.get_me_page).text
