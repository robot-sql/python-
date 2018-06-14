#!/usr/bin/env python
# coding=utf-8
import os

# 判断目录下是否有日志文件，有就删除
if os.path.exists('E:\\log.log') is True:
    os.remove('E:\\log.log')
# 测试输出日志
# py_file_list = ('step1_cookies.py', 'step2_cookies.py', 'step3_cookies.py', 'step4_cookies.py', 'step5_cookies.py')
py_file_list = ('step2_export.py', 'step3_rename.py', 'step4_excel_copy.py', 'step5_cy_imp.py')
for py_file in py_file_list:
    ex_py_file = 'python ' + py_file + ' >> E:\\log.log'
    os.system(ex_py_file)
