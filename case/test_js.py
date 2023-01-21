# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/yoyoketang/p/")
time.sleep(3)

# 第一个方法
# js：都是用document，相当于driver.XXX
# 只在火狐生效，chrome不生效；Fifefox使用documentElement，Chrome使用document.body
'''
document：就是一个元素；
documentElement：就是一个滚动条；
scrollTop：滚动的高度（从0到10000）
最底部：scrollTop=10000
最顶部：scrollop=0
'''
js1 = "document.documentElement.scrollTop=10000" # 在python里面是字符串"str"
driver.execute_script(js1) # 执行js脚本
# chrome上生效的写法
js_chrome = "document.body.scrollTop=10000"
driver.execute_script(js_chrome)
'''
"var = q=document.documentElement.scrollTop=0"
这个写法也是可以的，不过这个方法在chrome浏览器上也不管用
'''

# 第二个方法
# 在两个浏览器中都生效
'''
括号里面是两个参数，第一个参数是横坐标（0），第二个参数是纵坐标（10000）；
第一个参数是控制横向进度，第二个参数是控制纵向进度；
分号;代表有多个js语句的时候，用分号隔开，如果只有一条，可以不加
'''
js_all1 = "window.scrollTo(0,10000);" # 拉到底部
js_all2 = "window.scrollTo(0,0);" # 拉到顶部

# 第三个方法，这个方法最实用，上面两个方法稍微了解即可
# scrollHeight：自动获取高度，可以计算滚动条的高度，定位到最底部；两个浏览器都通用
js_height = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js_height)