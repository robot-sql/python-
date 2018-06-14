#!/usr/bin/env python
# coding=utf-8
import time
from selenium import webdriver
import os
import traceback
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# import requests
# from selenium.webdriver.common.keys import Keys


# 自动化操作创研系统的线索导入功能
def ui_auto_operation():
    # 模拟登陆
    # rep = requests.Session()
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)  # 设置隐性等待,等待10S加载出相关控件再执行之后的操作
    browser.maximize_window()
    browser.get('http://www.mangoauto.com.cn/SysPages/Login.aspx')
    time.sleep(5)  # 强制等待一般只用于测试
    browser.refresh()
    time.sleep(5)
    # 输入用户名
    username = browser.find_element_by_xpath('//*[@id="txtUserName"]')
    username.clear()
    username.send_keys('11*****')
    print('username input success')
    # 输入密码
    browser.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('11****')
    print('password input success')
    # # 加载验证码
    # yzm = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/dl[3]/dd/input')
    # yzm.send_keys(input('输入验证码:'))
    # 点击登陆
    browser.find_element_by_xpath('//*[@id="btnLogin"]').click()
    print('login success')
    # cookies = browser.get_cookies()
    # for cookie in cookies:
    #    rep.cookies.set(cookie['name'], cookie['value'])
    # 爬取对应网页的数据
    browser.current_window_handle
    browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[8]/div/a/span').click()
    # 切换到当前窗口
    browser.current_window_handle
    # time.sleep(5)
    tow_drive = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[8]/ul/li[5]/a')
    tow_drive.click()
    print('turn success')
    browser.current_window_handle
    # time.sleep(2)
    # 切换到iframe框架里面
    browser.switch_to.frame(browser.find_element_by_xpath('//*[@id="mainFrame"]'))
    # # 输入框只读属性的修改
    # js = 'document.getElementById("Text1").removeAttribute("readonly");'
    # browser.execute_script(js)
    # # 定位并且输入路径数据
    # receiveStart = browser.find_element_by_xpath('//*[@id="Text1"]')
    # receiveStart.clear()
    # receiveStart.send_keys('C:\\fakepath\\5096.xls')
    # # receiveStart.send_keys(Keys.RETURN)
    # 点击上传文件按钮
    browser.find_element_by_xpath('//*[@id="btn1"]').click()
    # 调用写好的exe实现上传
    os.system("C:\\fakepath\\autoup.exe")
    # time.sleep(5)
    load = browser.find_element_by_xpath('//*[@id="btn_lead"]')
    load.click()
    try:
        # 每隔2s就去扫描弹出框是否存在,总时长是300s,存在就继续执行之后代码
        WebDriverWait(browser, 300, 2).until(EC.alert_is_present())
        # 处理弹出alert框
        alert = browser.switch_to.alert
        alert.accept()
        if os.path.exists(r'C:\\fakepath\\5096.xls') is True:
            os.remove(r'C:\\fakepath\\5096.xls')
    finally:
        browser.close()
        # browser.quit()


if __name__ == '__main__':
    # @version : 3.4
    # @Author  : robot_lei
    # @Software: PyCharm Community Edition
    # @Features: 芒果汽车有限公司内部用于自动化操作创研系统导入功能
    log_path = 'C:\\fakepath\\log.log'
    logging.basicConfig(filename=log_path)
    try:
        ui_auto_operation()
    except Exception as e:
        s = traceback.format_exc()
        print(e)
        tra = traceback.print_exc()
