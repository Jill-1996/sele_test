# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Gloria/Desktop/div.html")

'''
内嵌div
1、先定位div的位置
2、再通过scrollTop（纵向）和scrollLeft（横向）方法控制进度
'''

# 纵向底部
# 获取id是单个元素，因为一个页面上id是唯一的
#js = 'document.getElementById("yoyoketang").scrollTop=10000'
# 获取的class是多个，取list的第一个对象
js = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js)

# 控制横向滚动条位置
js0 = 'document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js0)




