from PageLocators.home_page_locs import HomePageLoc as lc
from TestDatas import Common_Datas as cd
import time

from PageLocators.login_page_locs import LoginPageLoc as loc
from Common.basepage import BasePage


class IndexPage(BasePage):
    def if_user_is_exist(self):
        """
        判断元素是否存在
        :return:
        """
        try:
            self.wait_element_visible(lc.user_logo, "首页_判断用户是否存在")

        except TimeoutError:
            return False

        else:
            return True

    # 课程是否存在 - 通过课程id
    def course_id_exist(self, course_id):
        time.sleep(20)
        course_link = (lc.course_name_link[0], lc.course_name_link[1].format(course_id))
        try:
            self.wait_element_visible(course_link, "首页_判断课程是否创建成功")
        except:
            return False
        else:
            return True

    # 是否进入课程
    def if_enter_class(self):
        try:
            self.wait_element_visible(lc.hudong_link,"首页_等待互动链接出现")
            self.wait_element_visible(lc.zuoye_link,"首页_等待作业链接出现")
            self.wait_element_visible(lc.huati_link,"首页_等待首页话题链接出现")
            self.wait_element_visible(lc.ziliao_link,"首页_等待资料链接出现")
        except:
            return False

        else:
            return True

    # 是否能够看到创建成功
    def if_create_topic(self):
        try:
            self.wait_element_visible(lc.content, "首页_等待内容出现")
        except:
            return False
        else:
            return True

    # 是否编辑成功
    def if_edit_topic(self):
        try:
            self.wait_element_visible(lc.content,"首页_等待内容出现")
        except:
            return False
        else:
            return True

    # 是否删除成功
    def if_delete_topic(self):
        try:
            self.wait_element_visible(lc.tip_to_topic, "首页_等待话题提示出现")

        except:
            return False

        else:
            return True

    # ======================  学员角色  对应的操作 ============================
    # 加入课程当中
    def add_in_course(self, course_code):

        # 加课
        self.wait_element_visible(lc.add_class_button, "首页_等待添加课程按钮")
        self.click_element(lc.add_class_button, "首页_点击添加课程按钮")

        # 输入加课码
        self.wait_element_visible(lc.course_code_input, "首页_等待课程码输入框")
        self.input_text(lc.course_code_input,course_code, "首页_输入课程码")

        # 确认按钮
        self.click_element(lc.add_in_course_confirm_button, "首页_点击添加确认按钮")

    # 点击可传给你名称，进入课程页面
    def enter_in_class(self, course_id):
        time.sleep(10)
        course_name_link = (lc.course_name_link[0], lc.course_name_link[1].format(course_id))
        self.wait_element_visible(course_name_link, "首页_等待课程名称链接显示")
        self.click_element(course_name_link, "首页_点击课程名称链接")

    # 添加话题
    def create_topic(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.huati_link))
        # self.driver.find_element(*loc.huati_link).click()
        # self.driver.find_element(*loc.topic_create_button).click()
        # self.driver.find_element(*loc.topic_title_input).send_keys(cd.topic[0])
        # self.driver.find_element(*loc.topic_content_input).send_keys(cd.topic[1])
        # self.driver.find_element(*loc.topic_confirm_button).click()
        self.wait_element_visible(lc.huati_link, "课题细节页面_等待话题链接")
        time.sleep(5)
        self.click_element(lc.huati_link, "课题细节页面_点击话题链接")
        self.click_element(lc.topic_create_button, "课题细节页面_点击话题创建按钮")
        time.sleep(5)
        self.input_text(lc.topic_title_input, cd.topic[0],"课题细节页面_等待话题题目输入框" )
        self.input_text(lc.topic_content_input, cd.topic[1],"课题细节页面_话题创建确认按钮" )
        self.click_element(lc.topic_confirm_button, "课题细节页面_话题创建确认按钮")
        self.driver.refresh()

    def edit_topic(self):
        self.click_element(lc.topic_option, "课程细节页面_点击创建的话题")
        self.click_element(lc.topic_edit, "课程细节页面_点击编辑按钮")
        time.sleep(5)
        self.get_element(lc.topic_title_input, "课程细节页面_清空话题题目输入框").clear()
        self.get_element(lc.topic_content_input,"课程细节页面_清空话题内容输入框").clear()
        self.input_text(lc.topic_title_input, cd.topic[1], "课程细节页面_输入话题题目输入框")
        self.input_text(lc.topic_content_input, cd.topic[0],"课程细节页面_输入话题内容输入框")
        self.click_element(lc.topic_confirm_button, "课程细节页面_点击 编辑确认按钮")
        self.driver.refresh()
        time.sleep(5)

    def delete_topic(self):
        self.wait_element_visible(lc.topic_option, "课程细节页面_等待话题选项")
        self.click_element(lc.topic_option, "课程细节页面_点击话题选项")
        self.click_element(lc.topic_delete, "课程细节页面_点击话题删除")
        time.sleep(5)
        self.click_element(lc.topic_delete_confirm_button, "课程细节页面_点击话题确认删除按钮")
