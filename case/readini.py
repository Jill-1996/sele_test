# coding:utf-8

'''
专门写个读取配置文件的方法
'''
# 导入configparser
import configparser

# 先创建一个对象，去读取configparser
conf = configparser.ConfigParser
# 读的话用read;在同一路径就不用写路径了，直接写文件名，不同路径就写
conf.read("cfg.ini", "encoding='utf-8'")  # python2不需要加encoding='utf-8'，python3需要加encoding='utf-8'
# email：等于section；第二个参数：key值（email）
smtp_server = conf.get("email", "smtp_server")
print(smtp_server)
sender = conf.get("email", "sender")
print(sender)
psw = conf.get("email", "psw")
print(psw)
receiver = conf.get("email", "receiver")
print(receiver)
port = conf.get("email", "port")
print(port)
