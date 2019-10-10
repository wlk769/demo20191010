import time
import pytest
from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file

class TestLogin:
    def setup(self):
        self.driver = init_driver(no_reset=False)
        self.page = Page(self.driver)
    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize('args',analyze_file("login_data.yaml",'test_login'))
    def test_login(self,args):

        username = args['username']
        password = args['password']
        toast = args['toast']



        self.page.homepage.click_me_btn()

        self.page.zhucepage.click_btn_ok_me()

        self.page.loginpage.input_username(username)
        self.page.loginpage.input_password(password)
        self.page.loginpage.click_button()

        if  toast is None:
            assert self.page.mepage.get_me_page_me() == username
        else:
            assert self.page.loginpage.is_toast_exist(toast)
