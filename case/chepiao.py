# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()

# 为了方便调试方便，直接进编辑界面‘
driver.get("https://kyfw.12306.cn/otn/index/init")

'''
日历控件readonly；js修改属性
1、先去除元素的readonly属性
2、执行js脚本
3、清空输入框
4、输入时间
'''

# # 去掉元素的readonly（readonly：只能读），该语法固定
# js = "document.getElementById('train_date').removeAttribute('readonly')"
# driver.execute_script(js) # 执行js脚本

'''
如果相同时执行两个语句，可以在第一条语句后面加分号;
'''
# js1 = "document.getElementById('train_date').removeAttribute('readonly'); \
#      document.getElementById('train_date').value='readonly'" # 重新赋值
# driver.execute_script(js1) # 执行js脚本

# # 参数化
# # id是python里面的保留关键字，不能用id，区分开就加个下划线
# id_ = "train_date" # 先要把元素变成参数化就要先写出该元素，再参数化：%s
# js = "document.getElementById('%s').removeAttribute('readonly')"%id()
# driver.execute_script(js) # 执行js脚本

# 去掉后，也可以重新赋值
js1 = "document.getElementById('train_date').removeAttribute('readonly')"
js2 = "document.getElementById('train_date').value='readonly'" # 重新赋值
driver.execute_script(js2) # 执行js脚本

# 清空文本后输入内容
driver.find_element_by_id("train_date").clear() # 清空输入框
driver.find_element_by_id("train_date").send_keys("2023-01-20") # 输入时间


