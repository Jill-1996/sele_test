# coding:utf-8

from selenium import webdriver
import time

'''
switch处理iframe问题
switch方法需要先切换到iframe上，操作完之后又得切回来，很容易忘记切回来，操作比较繁琐
'''

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/cgi-bin/frame_html?sid=RtNpUREZ4Tb8UXoZ&r=c7f953fdf18a799667b2db60746bfc4d&lang=zh")
# 为了调试方便，等待十秒，手动点登录
time.sleep(3)
driver.find_element("class", "login_loginBox_tab_item").click()
driver.find_element("id", "img_out_735527061").click()
driver.find_element("id", "composebtn").click()
time.sleep(2)

'''
有富文本的直接用body里面的元素（例如：id，claas，name，然后直接sendkeys）
'''

# 切换iframe（第一次切换）
driver.switch_to.frame("mainFrame")
# 定位元素富文本
# driver.find_element_by_css_selector("#scAreaCtrl>.adddr_text>.js_input").send_keys("735527061@qq.com")
# driver.find_element("css", "#scAreaCtrl>.adddr_text>.js_input").send_keys("122@qq.com")
time.sleep(3)
# 输入主题
driver.find_element_by_id("subject").send_keys("主题")
# driver.find_element("id", "subject").send_keys("主题")
time.sleep(3)

# 第二次切换iframe
elem = driver.find_element_by_xpath("//iframe")
driver.switch_to.frame(elem) # 有id写id，有name写name，有索引就写索引（有一个就写0），没有就用上面的标签元素定位到后，返回的值
# 输入正文
driver.find_element_by_css_selector("accesskey='q'").send_keys("中文")
# driver.find_element("css", "accesskey='q'").send_keys("中文")

# 切出iframe
driver .switch_to.default_content()










