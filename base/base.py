from selenium import webdriver
# Base类中用于抽取常用的公共方法，并进行封装
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化方法
    def __init__(self):
        self.driver = webdriver.Firefox();
        self.driver.maximize_window();
        self.driver.get('http://cal.apple886.com');
        pass

    # 方法1：查找元素方法 加上显式等待(推荐使用)
    def base_find1(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 方法2：查找元素方法 加上隐式等待
    def base_find(self, loc): # 传过来的loc参数是一个元组形式，而find_element(By.ID,"#abcd")方法有两个形参 因此必须进行解包传参才可以使用
        self.driver.implicitly_wait(30)
        return self.driver.find_element(*loc)

    # 获取文本框的值
    def base_get_value(self, loc):
        # 获取文本框中输入的值value
        return self.base_find(loc).get_attribute("value");

    # 点击元素
    def base_click(self, loc):
        self.base_find(loc).click()
