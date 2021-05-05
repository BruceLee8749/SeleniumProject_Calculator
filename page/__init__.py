# 这里面是配置数据 __init__.py相当于一个包 目的是：导入文件时方便 直接文件夹.xxxx即可
from selenium.webdriver.common.by import By

# 加号按钮
calc_add = (By.CSS_SELECTOR, '#simpleAdd')
# 等号按钮
calc_eq = (By.CSS_SELECTOR, '#simpleEqual')
# 结果按钮
calc_result = (By.CSS_SELECTOR, '#resultIpt')
# 清屏按钮
calc_clear = By.CSS_SELECTOR, '#simpleClearAllBtn'

# tips： By.CSS_SELECTOR,'#simpleClearAllBtn' 这和加括号一样的语法，均表示元组
