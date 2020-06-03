# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium import webdriver

from PageLocators.login_page_locs import LoginPageLoc as loc
from Common.basepage import BasePage


class LoginPage(BasePage):
    # 用户输入框

    # # 公共变量
    # def __init__(self, driver: WebDriver):
    #     self.driver = driver
    #     self.wait = WebDriverWait(self.driver, 20)

    # 登陆行为
    def login(self, username, passwd):
        self.input_text(loc.user_input, username, "登录页面_输入用户名")
        self.input_text(loc.passwd_input, passwd, "登录页面_输入密码")
        self.click_element(loc.login_button, "登录页面——点击登录按钮")
        # self.wait.until(EC.visibility_of_element_located(loc.user_input))
        # self.driver.find_element(*loc.user_input).send_keys(username)
        # self.driver.find_element(*loc.passwd_input).send_keys(passwd)
        # self.driver.find_element(*loc.login_button).click()

    # 获取异常信息的行为
    def get_error_msg(self):
        # self.wait_element_visible(loc.error_msg, "登录页面_未输入密码")
        return self.get_element_text(loc.error_msg, "登录页面_获取错误提示")
        # self.wait.until(EC.visibility_of_element_located(loc.error_msg))
        # return self.driver.find_element(*loc.error_msg).text
