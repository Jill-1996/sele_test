# coding:utf-8

from selenium import webdriver
import time

'''
js处理iframe问题
js处理iframe无需先切换到iframe上，再切回来操作
它可以在iframe上和主页面上来回自由操作---这是js的强大之处
'''

# 加载配置文件，是为了免登录
profilepath = r"C://Users\Gloria\AppData\Roaming\Mozilla\Firefox\Profile" # 双引号是配置文件：故障报修
profile = webdriver.ChromeOptions(profilepath)
driver = webdriver.Chrome(profile)

# 为了调试方便，直接进编辑界面
driver.get("https://i.cnblogs.com/EditPosts.aspx?opt=1")
time.sleep(2)
# bodytext = "hao123" # 如果想要参数化，这里就要%s

# 输入富文本的内容，第一步切换iframe（输入富文本的内容参考qqemail，直接写js语句）
'''
第一步定位iframe元素
.contentWindow.document是切换过去
'''
# 第一种用body定位
js_edit1 = "document.getElementById('Editor_Edit_EditorBody.ifr')" \
          ".contentWindow.document.body.innerHTML='hao123'"

# js_edit01 = "document.getElementById('Editor_Edit_EditorBody.ifr')" \
#           ".contentWindow.document.body.innerHTML='%s'"%bodytext # 如果想要参数化，这里就要%s

# 第二种用id定位（这个里面有两层iframe）
js_edit2 = "document.getElementById('Editor_Edit_EditorBody.ifr')" \
          ".contentWindow.document.getElementById('tinymce').innerHTML='hao123'"

'''
selenium是用driver.findElement定位；
js是用document.getElementById定位，定位到iframe，定位到之后，切换到iframe里面去
切换到iframe里面，js的语法是：contentWindow，切换过去后，继续定位
innerHTML：插入html富文本内容；输入的内容想要参数化，用%s代替
'''

# 选择上述两种方法执行js
driver.execute_script(js_edit1)

'''
以上写法只是专门处理富文本（有iframe）相关的问题，其他地方遇到iframe不一定通用
'''

'''
js获取元素的几种方法：
1.通过id获取
document.getElementById(“id”)----------获取的是单个
2.通过name获取
 document.getElementsByName(“Name”)[0]---------获取的是多个
 要取多个，就用下标，第一个是0
返回的是list 
3.通过标签名选取元素
document.getElementsByTagName(“tag”) --------获取的是多个
4.通过CLASS类选取元素
document.getElementsByClassName(“class”) --------获取的是多个
兼容性：IE8及其以下版本的浏览器未实现getElementsByClassName方法
5.通过CSS选择器选取元素
document.querySelectorAll(“css selector")
兼容性：IE8及其以下版本的浏览器只支持CSS2标准的选择器语法 
'''




