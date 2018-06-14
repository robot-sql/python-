#!/usr/bin/env python
# coding=utf-8
import os

# 读取文件并且重新命名
# 获取该目录下所有文件，存入列表中
path = 'E:\\load_bi\\tmp\\'
new_path = 'E:\\load_bi\\new_tmp\\'
f_name_s = os.walk(path)
# 新文件名称存入列表
lead_list = ('车库线索', '降价通知', '详情页未登录线索', '分期工具', '首页弹窗', '预约看车', '微信小程序', '询价')
# lead_list = ('车库线索', '降价通知')
# 设置新文件名
new_name_list = [lead_new_name for lead_new_name in lead_list]
print(new_name_list)
# 旧文件名称存入列表
# for root, dirs, files in f_name_s:
#     # 读取旧文件名称
#     old_name_list = [f_name for f_name in files]
old_name_list = os.listdir(path)
# 通过名称第五位到后五位之间截取的字符串转整数排序
old_name_list.sort(key=lambda x: int(x[5:-4]))
print(old_name_list)
# 通过获取列表数据来对应命名
f_cnt = os.listdir(path)
i = 0
for i in range(len(f_cnt)):
    print(i)
    old_name = path+old_name_list[i]
    new_name = new_path+new_name_list[i]+'.xls'
    # 用os模块中的rename方法对文件改名
    os.rename(old_name, new_name)
    i = i+1
    print(old_name, '======>', new_name)


