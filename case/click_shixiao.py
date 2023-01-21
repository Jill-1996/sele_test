# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()

'''
有些时候click事件会失效，如点击百度设置的保存设置按钮
解决办法：1.先点击父元素，找回焦点
解决办法：2.用js去执行点击事件
解决办法：3.jqeury语法去点击
'''
# 解决办法1（先点父元素）
driver.find_element("id", "gxszButton").click()
driver.find_element("class name", "prefpanelgo").click()

# 解决办法2（用js直接去点击）
js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)

# 解决办法3（jquery语法去点击）
Jquery = "$('css selector').click()"
driver.execute_script(Jquery)




