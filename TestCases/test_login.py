import unittest
from selenium import webdriver
import ddt
from PageObject.login_page import LoginPage
from PageObject.index_page import IndexPage
from TestDatas import Common_Datas as cd, login_data as ld
import warnings


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        # 打开谷歌浏览器，访问课堂派网址
        warnings.simplefilter('ignore', ResourceWarning )
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(cd.login_url)
        self.lp = LoginPage(self.driver)
        pass

    def tearDown(self):  # self 指的是实例名
        # 退出浏览器会话
        self.driver.quit()
        pass

    def test_01_login_success(self):
        # 登陆页面-输入用户名
        # 登陆页面-输入密码
        # 登陆页面-点击登陆按钮
        self.lp.login(ld.normal_data["user"], ld.normal_data["passwd"])
        # 断言
        # 首页-获取元素，确认是否存在
        self.assertTrue(IndexPage(self.driver).if_user_is_exist())

    @ddt.data(*ld.incorrect_datas)
    def test_02_login_abnormal(self, data):
        self.lp.login(data["user"], data["passwd"])
        self.assertEqual(data["check"], self.lp.get_error_msg())


if __name__ == '__main__':
    unittest.main()


