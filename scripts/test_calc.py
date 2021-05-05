# 测试业务方法

# Tips：再次梳理    1. base里面放base，元素通用方法（点击，查找。。）2.page里面实现人工模拟点击 3.scripts里面实现unittest测试

import unittest
from parameterized import parameterized
from tools.readjson import readJson

from page.page_calc import PageCalc


# 对于数据量较大的情况用文件json或者txt
def get_data():
    readjson = readJson()
    list_json_file = readjson.readJson()
    return list_json_file

class TestCalc(unittest.TestCase):
    # 类级别初始化方法
    @classmethod
    def setUpClass(cls):
        # 获取PageClass对象
        cls.calc = PageCalc()

    # 类级别结束方法
    @classmethod
    def tearDownClass(cls):
        # 退出浏览器
        # cls.calc.driver.quit()
        pass

    # 测试加法计算  数据参数化：就是将若干组实参数据data 直接传给形参
    @parameterized.expand(get_data())
    def test_calc(self, a, b, expect):
        print('{}+{}={}:'.format(a, b, self.calc.page_get_value()))
        # 调用计算组合方法，直接断言最后结果是否符合预期
        self.calc.page_calc(a, b)
        self.assertEqual(expect, float(self.calc.page_get_value()))


if __name__ == '__main__':
    unittest.main(verbosity=2)
