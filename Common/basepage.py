# 1.封装基本关键字，任何一个页面操作都可以捕获异常/输出操作日志/失败
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from PageLocators.home_page_locs import HomePageLoc as loc
from TestDatas import Common_Datas as cd
import time
import logging
from datetime import datetime

from Common.dir_config import screenshot_dir


class BasePage:


    # 元素定位、 元素操作
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_element_visible(self, loc, img_doc, timeout=20, frequency=0.5):
        logging.info("在{}等待元素{}可见。".format(img_doc, loc))
        start_time = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面或者哪个模块出错了。
            # 异常日志捕获
            self.save_screenshot(img_doc)
            logging.exception("等待元素可见失败。")
            raise
        else:
            end_time = time.time()
            logging.info("等待时长为:{}".format(end_time - start_time))

    # def wait_page_contain_element(self, loc, img_doc, timeout=20, frequency=0.5):
    #     # try:
    #     #     WebDriverWait(self.driver, timeout, frequency).until(EC.invisibility_of_element_located(loc))
    #     #
    #     # except:
    #     #
    #     # else:
    #     pass

    def get_element(self, loc, img_doc):
        logging.info("在{}查找元素{}。".format(img_doc, loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_screenshot()
            logging.exception("元素查找失败。")
            raise
        else:
            return ele

    def click_element(self, loc, img_doc, timeout=20, frequency=0.5):
        # 元素可见，要找到元素
        self.wait_element_visible(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        logging.info("在{}点击元素{}。".format(img_doc, loc))
        try:
            ele.click()
        except:
            # 异常截图 - 通过截图名称，知道是哪个页面模块出错了
            self.save_screenshot(img_doc)
            # 异常日志捕获
            logging.exception("元素点击失。")
            raise

    def input_text(self, loc, text, img_doc, timeout=20, frequency=0.5):
        self.wait_element_visible(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        try:
            ele.send_keys(text)
        except:
            self.save_screenshot(img_doc)
            logging.exception("元素输入文本失败。")
            raise
        else:
            logging.info("在{}对元素{}输入文本内容为：{}。".format(img_doc, loc, text))

    def get_element_text(self, loc, img_doc, timeout=20, frequency=0.5):
        self.wait_element_visible(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        try:
            text = ele.text
        except:
            self.save_screenshot(img_doc)
            logging.exception("获取元素文本输入失败。")
            raise
        else:
            logging.info("获取到的元素文本内容为：{}".format(text))
            return text

    def get_element_attr(self, loc, attr_name, img_doc, timeout=20, frequency=0.5):
        self.wait_element_visible(loc, img_doc, timeout, frequency)
        ele = self.get_element(loc, img_doc)
        try:
            ele_attr = ele.get_attribute(attr_name)
        except:
            self.save_screenshot(img_doc)
            logging.info("获取元素属性失败。")
            raise
        else:
            logging.info("获取到的元素文本属性为{}".format(ele_attr))
            return ele_attr

    def save_screenshot(self, img_doc):
        # 存储到指定目录下 - 加上路径配置
        t = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")  # t的格式是 年月日 时-分-秒
        filename = screenshot_dir + "{}_{}.png".format(t, img_doc)
        self.driver.save_screenshot(filename)
        logging.info("页面截图文件保存在：{}".format(filename))

    # 封装
    # iframe 切换
    # alert 关闭
    # 上传
    # select
    # 窗口切换
