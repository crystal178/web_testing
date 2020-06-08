import unittest
import warnings

from selenium import webdriver

from API.api_course_operator import CourseOper
from PageObject.index_page import IndexPage
from PageObject.login_page import LoginPage
from TestDatas import Common_Datas as cd
from TestDatas import course_datas as cod


class TestCourseDetail(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 老师通过接口创建课程
        warnings.simplefilter('ignore', ResourceWarning)
        c = CourseOper(*cd.teacher_user)
        cls.course_id, cls.course_code = c.add_courser(cod.course_name, cod.course_name)
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(cd.login_url)
        # 学生登录系统
        cls.lp = LoginPage(cls.driver)
        cls.lp.login(*cd.student_user)
        # 学生添加课程
        cls.ip = IndexPage(cls.driver)
        cls.ip.add_in_course(cls.course_code)
        # 学生进入课程
        cls.ip.enter_in_class(cls.course_id)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        c = CourseOper(*cd.teacher_user)
        c.delete_courser(cls.course_id, cd.teacher_user[1])

    def test_1_create_topic(self):
        # 创建新话题
        ip = IndexPage(self.driver)
        ip.create_topic()
        self.assertTrue(ip.if_create_topic())
        # 断言帖子存在

    def test_2_edit_topic(self):
        # 点击资料文字进行切换
        ip = IndexPage(self.driver)
        ip.edit_topic()
        self.assertTrue(ip.if_edit_topic())
        # 编辑内容
        # 编辑成功的断言
        pass

    def test_3_delete_topic(self):
        # 删除帖子
        ip = IndexPage(self.driver)
        ip.delete_topic()
        self.assertTrue(ip.if_delete_topic())
        # 删除成功的断言


if __name__ == '__main__':
    unittest.main()
