from selenium.webdriver.common.by import By


class LoginPageLoc:

    user_input = (By.XPATH, '//input[@name="account"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@name="pass"]')
    # 登陆元素
    login_button = (By.XPATH, '//*[contains(@class,"pt-login")]//a[@class="btn-btn"]')
    # 登陆表单曲 - 错误提示
    error_msg = (By.XPATH, '//p[@class="error-tips"]')