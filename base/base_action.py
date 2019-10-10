from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, content):
        self.find_element(feature).send_keys(content)

    def clear(self, feature):
        self.find_element(feature).clear()

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)

    def get_text(self, feature):
        return self.find_element(feature).text

    def  is_toast_exist(self,message):

        message_xpath = By.XPATH,"//*[contains(@text,'%s')]" % message

        try:
            self.find_element(message_xpath,5,0.1)
            return True
        except TimeoutException:
            return False


    def get_toast_text(self,message):
        if self.is_toast_exist(message):

            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")



