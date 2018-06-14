#!/usr/bin/env python
# coding=utf-8
import time
import datetime
import yaml
# import os
from selenium import webdriver
# import requests
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

# 实例化一个火狐配置文件
fp = webdriver.FirefoxProfile()
# 设置各项参数，参数可以通过在浏览器地址栏中输入about:config查看。
# 设置成0代表下载到浏览器默认下载路径；设置成2则可以保存到指定目录
fp.set_preference("browser.download.folderList", 2)
# 是否显示开始,(个人实验，不管设成True还是False，都不显示开始，直接下载)
fp.set_preference("browser.download.manager.showWhenStarting", False)
# 指定下载目录
fp.set_preference('browser.download.dir', 'E:\\load_bi\\tmp\\')
# 不询问下载路径；后面的参数为要下载页面的Content-type的值
# 文件类型参考 http://www.w3school.com.cn/media/media_mimeref.asp
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/vnd.ms-excel")
# 模拟登陆
browser = webdriver.Firefox(firefox_profile=fp)
browser.maximize_window()
browser.delete_all_cookies()
url = 'https://seller.mall.autohome.com.cn/saleClues/list'
browser.get(url)
# time.sleep(2)
# 读取保存到cookies文件到本地的路径
yamlPath = 'E:\\load_bi\\config.yaml'
f = open(yamlPath, 'r', encoding='utf-8')
cont = f.read()
conf = yaml.load(cont)
# 读取cookie值
cookies = conf.get("cookies")
# 添加cookie
for cookie in cookies:
    browser.add_cookie(cookie)
print("cookies")
print(browser.get_cookies())
time.sleep(5)
# 这里重新获取地址,因为有些系统,未登录状态,链接会跳转,这里就是,登录状态后,才能正确打开指定网址,所以这里要再次指定网址。
browser.get(url)
# 刷新查看登录状态
browser.refresh()
time.sleep(5)
# 爬取对应网页的数据
# _new_window = browser.current_window_handle
# one_drive = browser.find_element_by_xpath('/html/body/div[3]/div[2]/ul/li[3]/a').click()
# _new_two_window = browser.current_window_handle
# time.sleep(10)
# tow_drive = browser.find_element_by_xpath('//*[@id="SaleClues-Manager"]/a')
# tow_drive.click()
# # ActionChains(browser).double_click(one_drive).perform()
# print('turn success')
# 切换页面，修改接收时间控件的只读属性，然后再填写日期
detester = str(datetime.date.today())
_new_thr_window = browser.current_window_handle
# js = "$('input[id=receiveStart]').attr('readonly','')"
js = 'document.getElementById("receiveStart").removeAttribute("readonly")'
browser.execute_script(js)
receiveStart = browser.find_element_by_xpath('//*[@id="receiveStart"]')
receiveStart.clear()
receiveStart.send_keys(detester)
receiveStart.send_keys(Keys.RETURN)
js = 'document.getElementById("receiveEnd").removeAttribute("readonly")'
browser.execute_script(js)
receiveEnd = browser.find_element_by_xpath('//*[@id="receiveEnd"]')
receiveEnd.clear()
receiveEnd.send_keys(detester)
receiveEnd.send_keys(Keys.RETURN)
time.sleep(2)
# 线索类型的选择
# lead_list = ('车库线索', '降价通知', '详情页未登录线索', '分期工具', '首页弹窗', '预约看车','微信小程序', '询价')
lead_list = ('/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[9]/a',
             '/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[2]/a',
             '/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[45]/a',
             '/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[44]/a',
             '/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[42]/a',
             '/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[41]/a',
             '/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[39]/a',
             '/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[2]/ul/li[12]/a')
for lead in lead_list:
    # js = "document.getElementById('Title').style.display='block'"
    # browser.execute_script(js)
    sel = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/dl[1]/dd/div/div[1]/em")
    ActionChains(browser).double_click(sel).perform()
    sel_lead = browser.find_element_by_xpath(lead).click()
    # browser.find_element_by_link_text(lead).click()
    time.sleep(1)
    # 选择查询
    browser.find_element_by_xpath('//*[@id="btnQuery"]').click()
    time.sleep(5)
    # 点击导出文件按钮
    load = browser.find_element_by_xpath('//*[@id="btnExport"]')
    load.click()
print('download end')
time.sleep(15)
browser.quit()
# browser.close()

