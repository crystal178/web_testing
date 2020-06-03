from selenium.webdriver.common.by import By
from TestDatas import Common_Datas as cd


class HomePageLoc:
    user_logo = (By.ID, 'user')
    # ============================= 学员角色 ======================================

    #加入课程
    add_class_button = (By.XPATH, '//div[text()= "+ 加入课程"]')

    #加课程验证码输入框
    course_code_input = (By.XPATH, '//div[@class="chuangjiankc"]//input')

    #加课 - 加入按钮
    add_in_course_confirm_button = (By.XPATH, '//a[text()="加入"]')

    #课程div在页面的定位 - 为断言所用 - 通过课程的course_id - 需要替换定位中{}
    course_confirm = (By.XPATH, '//dl[@data-id="{}"]')

    #课程名字链接 - 通过课程的course_id - 需要替换定位中的{}
    course_name_link = (By.XPATH, '//dl[@data-id="{}"]//a[@class="jumptoclass"]')


    # 课堂进入页面存在的课堂互动元素，作业元素，话题元素，资料元素，测试(考试元素）， 公告元素

    hudong_link = (By.XPATH, '//a[text()="课堂互动"]')
    zuoye_link = (By.XPATH, '//a[text()="作业"]')
    huati_link =(By.XPATH, '//a[text()="话题"]')
    ziliao_link = (By.XPATH, '//a[text()="资料"]')
    ceshi_link = (By.XPATH, '//a[text()="测试(考试)"]')
    gonggao_link = (By.XPATH,'//a[text()="公告"]')


    # =====================  话题页面 ================================================
    topic_create_button = (By.XPATH, '//a[text()="发起新话题"]')
    topic_title_input = (By.XPATH, '//input[@placeholder= "话题标题，老师和学生都可以发起话题"]')
    topic_content_input = (By.XPATH, '//div[@contenteditable="true"]')
    topic_confirm_button = (By.XPATH, '//div[@class="opt-cont"]//a[text()="确定"]')
    topic_delete_confirm_button = (By.XPATH,'//div[@class="layui-layer-btn"]//a[text()="确定"]')
    topic_option = (By.XPATH, '//a[@class="opt-btn"]')
    topic_edit = (By.XPATH, '//a[text()="编辑"]')
    topic_delete = (By.XPATH, '//a[text()="删除"]')
    content = (By.XPATH, '//div[@class="announce-cont-box"]')
    # content = (By.XPATH, '//div[text()="{}..."]'.format(cd.topic[1]))
    # content_1 = (By.XPATH, '//div[text()="{}..."]'.format(cd.topic[0]))
    tip_to_topic =(By.XPATH, '//h3[text()="点击上方按钮，您可以发起新话题。"]')






