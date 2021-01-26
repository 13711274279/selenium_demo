import os
import time
from log.log import Log
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from commom.readini import readini

browser = readini("Browser", "Chrome")
# error_img = os.path.dirname('../error_img/')
error_img = os.path.dirname(os.path.dirname(__file__)) + "/error_img"
chromePath = os.path.dirname(os.path.dirname(__file__)) + "/driver/chromedriver.exe"
print(chromePath)


class Browser:
    browser_type = {
        "Chrome": webdriver.Chrome,
        "Firefox": webdriver.Firefox
    }

    def __init__(self):
        # 初始化
        self.browser = browser
        self.log = Log()
        try:
            if self.browser_type[browser]:
                self.driver = self.browser_type[browser](chromePath)
                self.wait = WebDriverWait(self.driver, 10, 0.2)
                self.driver.implicitly_wait(10)
        except ValueError as e:
            self.log.error(e)
        self.time = int(time.time() * 1000)

    def error_img(self, located):
        # 截图
        name = error_img + "/" + str(self.time) + '.png'
        self.log.error("错误的定位或其他异常。定位方式为：{}".format(located))
        return self.driver.get_screenshot_as_file(name)

    def open_windows(self, url):
        # 打开窗口
        self.driver.maximize_window()
        self.log.info("打开{}浏览器".format(self.browser))
        self.log.info("打开网页{}".format(url))
        return self.driver.get(url)

    def find_element(self, search, element):
        try:
            # 判断元素是否存在
            is_invisible = self.wait.until(EC.presence_of_element_located((search, element)), "Can't Find Element")
            self.log.info("找到元素{},定位方式为{}".format(element, search))
            return is_invisible
        except Exception as e:
            self.error_img(element)

    def send_message(self, search, element, message):
        # 输入字符
        element = self.find_element(search, element)
        element.send_keys(message)
        self.log.info("输入或上传文件：{}".format(message))

    def click_element(self, search, element):
        # 点击事件
        element = self.find_element(search, element)
        element.click()
        self.log.info("点击定位元素：{}".format(element))

    def select_element(self, search, element, text_name):
        # 下拉框事件
        element = self.find_element(search, element)
        element.click()
        Select(element).deselect_by_visible_text(text_name)

    def flash(self):
        # 刷新事件
        self.driver.refresh()
        self.log.info("{}".format("页面刷新"))

    @property
    def get_titile(self):
        # 获取当前页面标题
        return self.driver.title

    def get_text(self, search, element):
        # 获取文本值
        element = self.find_element(search, element)
        return element.send_keys

    def clear_text(self, search, element):
        # 清除文本框
        element = self.driver.find_element(search, element)
        element.clear()

    def close_broswer(self):
        # 关闭浏览器
        self.driver.close()
        self.log.info("关闭浏览器")