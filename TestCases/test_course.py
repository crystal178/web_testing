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

    # def setUp(self):
    #     warnings.simplefilter('ignore', ResourceWarning)
    #     # 1.保障游客加入的课程，并当前学生未加入该课程 --老师账号
    #     c = CourseOper(*cd.teacher_user)
    #     self.course_id, self.course_code = c.add_courser(cod.course_name, cod.course_name)
    #     # 2.以学生账号，登录系统
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get(cd.login_url)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.login(*cd.student_user)
    #     # self.wait = WebDriverWait(self.driver, 20)
    #     pass
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

        # self.wait.until(EC.visibility_of_element_located(HomePageLoc.add_class_button))
        # self.driver.find_element(*HomePageLoc.add_class_button).click()
        # # 首页：输入课程码
        # self.driver.find_element_by_xpath('//input[@placeholder= "请输入课程加课验证码"]').send_keys(self.course_code)
        # # 点击加入
        # self.driver.find_element_by_xpath('//a[text()= "加入"]').click()
        # # 断言
        # self.driver.quit()
        # pass


if __name__ == '__main__':
    unittest.main()
