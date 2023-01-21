# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/yoyoketang/p/")
time.sleep(3)

'''
聚焦元素：这个元素是万能的；
第一步是定位目标元素；
第二步执行js滚动到元素出现的位置
'''
ele = ("xpath", "//h3[texy()='最新评论']")
# 括号分号前面是聚焦，后面是聚焦到定位到的元素（ele）
driver.execute_script("arguments[0].scrollInttoView();", ele)
