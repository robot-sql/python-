#!/usr/bin/env python
# coding=utf-8
import time
import yaml
# import os
from selenium import webdriver
# import requests
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys


# 模拟登陆
browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://seller.mall.autohome.com.cn')
# time.sleep(2)
# 输入用户名
cookies = browser.get_cookies()
print(cookies)
username = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/dl[1]/dd/input')
username.clear()
username.send_keys('18700009577')
print('username input success')
# 输入密码
browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/dl[2]/dd/input').send_keys('1122222')
print('password input success')
# 加载验证码
yzm = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/dl[3]/dd/input')
yzm.send_keys(input('输入验证码:'))
# yzm.send_keys(Keys.RETURN)
# 加载 cookie
# browser.add_cookie({'name': 'JSESSIONID', 'value': '6c2fe815-9ffc-4973-985d-7ff4262c1dd4'})
# time.sleep(5)
# browser.refresh()
# 点击登陆
browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[2]/a').click()
print('login success')
time.sleep(10)
cookies = browser.get_cookies()
print(cookies)
# 设置保存的cookies文件到本地的路径
# fileNamePath = 'E:\\load_bi\\'
# 拼接config.yaml文件绝对路径
# yamlPath = os.path.join(fileNamePath, 'config.yaml')
yamlPath = 'E:\\load_bi\\config.yaml'
# 以覆盖写入打开文件
fw = open(yamlPath, 'w', encoding='utf-8')
# 构建数据
data = {"cookies": cookies}
# 装载写入yaml文件。
yaml.dump(data, fw)
# for cookie in cookies:
#     browser.cookies.set(cookie['name'], cookie['value'])
