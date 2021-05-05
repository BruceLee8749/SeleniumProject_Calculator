from selenium.webdriver.common.by import By
# 导入page包下的文件
import page
from base.base import Base


# page类继承了Base，实现对页面的操作  思路：具体怎么实现数字加减乘除无须关注。我要实现的是页面原本由人工点击，模拟成机器点击即可。
class PageCalc(Base):
    # 点击数字方法 如果数字为多位数将num拆分点击
    def page_click_num(self, num):
        for i in str(num):
            loc = By.CSS_SELECTOR, "#simple{}".format(i)
            self.base_click(loc)

    # 点击加号
    def page_click_add(self):
        self.base_click(page.calc_add)

    # 点击等号
    def page_click_eq(self):
        self.base_click(page.calc_eq)

    # 获取结果方法
    def page_get_value(self):
        return self.base_get_value(page.calc_result)

    # 清屏
    def page_click_clear(self):
        self.base_click(page.calc_clear)

    # 组合业务方法 执行数字加法并返回运行结果
    def page_calc(self,a,b):
        # 数字a
        self.page_click_num(a)
        # 加号
        self.page_click_add()
        # 数字b
        self.page_click_num(b)
        # 等号
        self.page_click_eq()

