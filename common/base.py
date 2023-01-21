# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化driver
    def __init__(self, driver, describe=None):
        self.driver = driver
        self.timeout = 30 # 30s
        self.poll = 0.5

    def findElement(self, loctor):
        '''
        args:
        loctor 传元组，如("id","xx")
        :param driver:
        :param loctor:
        :return:
        '''
        # element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*loctor))
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElementNew(self, loctor):
        # 找到了，返回的是element，没找到抛异常TimeoutException
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(loctor))
        return element

    def findElementsNew(self, loctor):
        # 找到了，返回的是list，没找到抛异常TimeoutException
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elements

    def findElenments(self, loctor):
        '''
        args:
        loctor 传元组，如("id","xx")
        :param driver:
        :param loctor:
        :return:
        '''
        # elements = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_elements(*loctor))
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_elements(*loctor))
        return elements

    def sendKeys(self, loctor, text):
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def click(self, loctor):
        ele = self.findElement(loctor)
        ele.click()

    def clear(self, loctor):
        ele = self.findElement(loctor)
        ele.clear()

    def moveToElement(self, loctor): # loctor就是定位元素这个方发
        '''鼠标悬停事件'''
        # mos = driver.find_element()  # element是元素对象
        # self.findElement是自己封装的查找元素的方法，调用自己写的封装的方法就行了，就可以不用driver.find_element()了
        mos = self.findElement(loctor)
        ActionChains(self.driver).move_to_element(mos).perform() # mos就是element的元素对象

    # >XXX<,大于号小于号之间的文本就是文本属性；tag是标签属性，class...是常规属性
    def is_text_in_element(self, locator, text):
        '''判断给定的text在这个元素的文本上
        要么返回true,要么返回false,不要让它抛异常了
        '''
        # try：尝试去找元素，如果成功了，返回结果；rusule返回布尔值（true，false），成功就返回结果（resule）
        try:
            # WebDriverWait：循环去判断
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element(locator, text))
            return result
        # except：找不到元素，返回false
        except:
            return False

    def is_value_in_element(self, locator, value):
        '''判断给定的value在这个元素的文本上
        要么返回true,要么返回false,不要让它抛异常了
        三种情况为假：0，""（空字符串）, None（为假的时候，返回false）  python是没有null的
        1.找不到元素返回False
        2.value为空返回False
        3.value不在元素的value值里返回False
        '''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_element_exsits(self, locator):
        '''判断元素是否存在；查找元素的时候，存在返回element，不存在的时候Timeout就抛异常了'''
        # try：尝试去查找元素，只要找到了，就认为这个元素存在，就返回ture，不存在，except返回false
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_alert_exsit(self, timeout=5):
        '''判断alert弹窗是否存在；语文老师教的：直到，，，才，，，（EC是一句固定的话，直到XXX才XXX）
        如有alert,返回的是alert对象，
        没有就返回False'''
        alert = WebDriverWait(self.driver, timeout, self.poll).until(EC.alert_is_present())
        return alert

    # 封装js1，方便后面调用
    def js_scroll_end(self):
        '''
        滚到到底部
        :return:
        '''
        js_height = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js_height)

    # 封装js2，方便后面调用
    def js_focus(self, loctor):
        '''
        聚焦元素
        :param loctor:
        :return:
        '''
        # targe：目标元素
        targe = self.findElement(loctor) # 先调用前面封装定位的方法
        # 括号里面分号前是写死的，不用管
        self.driver.execute_script("arguments[0].scrollInttoView();", targe)

    # 封装js3，方便后面调用
    def js_scroll_top(self):
        '''
        滚到到顶部
        :return:
        '''
        js = "window.scrollTo(0, 0)"
        driver.execute_script(js)

    # 封装执行js脚本，方便后面调用
    def js_execute(self, js):
        # 执行js
        self.driver.execute_script(js)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    # 实例化Base
    base = Base(driver)
    loc1 = ("id", "kw") # 定位百度输入框（先定位元素，再去调用查找元素这个方法）
    # e1e1 = findElenment(driver, "id", "kw")
    # e1e1 = base.findElenment(loc1)
    # e1e1.send_keys("hello")
    # 合并上面两步为一步
    base.sendKeys(loc1, "发送的内容") # 关键字

    loc2 = ("css selector", "#su") # 定位搜索按钮（先定位元素，再去调用查找元素这个方法）
    # e1e2 = findElenment(driver, "css selector", "#su")
    # e1e2 = base.findElenment(loc2)
    # e1e2.click()
    # 合并上面两步为一步
    base.click(loc2)


    # def is_text_in_element(self, locator, text):
    news_loc = ("xpath", ".//*[@id='ul']/a[1]") # 新闻
    res = base.is_text_in_element(news_loc, "新闻")
    print(res)

    # def is_value_in_element(self, locator, value):
    btn_loc = ("id", "su")
    res1 = base.is_value_in_element(btn_loc, "百度一下")
    print(res1)

    driver.get("http://www.cnblogs.com/yoyoketang/p/")
    import time
    time.sleep(3)
    base.js_scroll_end() # 滚动到底部

    plun_loc = ("xpath", "//h3[texy()='最新评论']")
    base.js_focus(plun_loc)