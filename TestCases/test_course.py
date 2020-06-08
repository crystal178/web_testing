import time
import unittest
import warnings

from selenium import webdriver

from API.api_course_operator import CourseOper
from PageObject.index_page import IndexPage
from PageObject.login_page import LoginPage
from TestDatas import Common_Datas as cd
from TestDatas import course_datas as cod


class TestCourse(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        c = CourseOper(*cd.teacher_user)
        cls.course_id, cls.course_code = c.add_courser(cod.course_name, cod.course_name)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(cd.login_url)
        cls.lp = LoginPage(cls.driver)
        cls.lp.login(*cd.student_user)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_1_add_in_course(self):
        # 在首页，点击 加入课程 按钮
        # 首页：输入课程码
        # 点击加入
        # 断言
        ip = IndexPage(self.driver)
        ip.add_in_course(self.course_code)
        self.assertTrue(ip.course_id_exist(self.course_id))

    def test_2_enter_in_class(self):
        # 点击课程链接，进入课程
        ip = IndexPage(self.driver)
        ip.enter_in_class(self.course_id)
        time.sleep(10)
        # 断言
        self.assertTrue(ip.if_enter_class())


if __name__ == '__main__':
    unittest.main()
