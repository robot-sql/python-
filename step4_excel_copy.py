#!/usr/bin/env python
# coding=utf-8
import os
import xlrd
import shutil
from xlutils.copy import copy
import datetime
import logging
import traceback


class excel_cp:
    def __init__(self, ):
        day = datetime.date.today()
        self.str_day = str(day).replace('-', '')

    # 处理excel合并
    def excel_merge(self, old_name, new_name):
        if old_name == '降价通知.xls':
            lead_source = 'r510'
        elif old_name == '400溢出.xlsx':
            lead_source = 'r880'
        elif old_name == '潜客推荐.xlsx':
            lead_source = 'r722'
        elif old_name == '详情页未登录线索.xls':
            lead_source = 'r995'
        elif old_name == '分期工具.xls':
            lead_source = 'r994'
        elif old_name == '首页弹窗.xls':
            lead_source = 'r993'
        elif old_name == '微信小程序.xls':
            lead_source = 'r992'
        elif old_name == '预约看车.xls':
            lead_source = 'r991'
        elif old_name == '询价.xls':
            lead_source = 'r990'
        elif old_name == '车库线索.xls':
            lead_source = 'r520'
        old_dir = 'E:\\load_bi\\' + self.str_day + '\\' + old_name
        new_dir = 'E:\\load_bi\\' + self.str_day + '\\' + new_name
        # 打开要使用的excel,获取要需要写入的行数
        bk = xlrd.open_workbook(old_dir)
        sh = bk.sheet_by_name("Page 1")
        nrows = sh.nrows
        # 打开要插入的excel,获取sheet页面的行数,再获取输入的sheet
        oldWb = xlrd.open_workbook(new_dir, formatting_info=True)
        in_sheet = oldWb.sheet_by_name("Sheet1")
        in_nrows = in_sheet.nrows
        newWb = copy(oldWb)
        sheet = newWb.get_sheet(0)
        # if nrows >= 1:
        for i in range(1, nrows):
            row_data = sh.row_values(i)
            # doc = open('E:\\load_bi\\' + self.str_day + '\\log.log', 'w')
            print(row_data)
            for j in (in_nrows-1+i, i+in_nrows-1):
            # ---------写出文件到excel--------
                print("-----正在往j写入 " + str(j) + " 行")
                sheet.write(j, 0, label=sh.cell_value(i, 4))   # 将old_dir的第i行第5列数据写入到new_dir第j行第1列
                sheet.write(j, 1, label=sh.cell_value(i, 1))   # 将old_dir的第i行第2列数据写入到new_dir第j行第2列
                sheet.write(j, 3, lead_source)                 # 将指定数据写入到new_dir第2行第4列
                sheet.write(j, 14, label=sh.cell_value(i, 2))  # 将old_dir的第i行第3列数据写入到new_dir第j行第15列
                sheet.write(j, 15, label=sh.cell_value(i, 3))  # 将old_dir的第i行第4列数据写入到new_dir第j行第16列
                sheet.write(j, 27, label=sh.cell_value(i, 7))  # 将old_dir的第i行第8列数据写入到new_dir第j行第28列
                sheet.write(j, 28, label=sh.cell_value(i, 8))  # 将old_dir的第i行第9列数据写入到new_dir第j行第29列
                sheet.write(j, 29, label=sh.cell_value(i, 9))  # 将old_dir的第i行第10列数据写入到new_dir第j行第30列
                sheet.write(j, 10, label=sh.cell_value(i, 10))  # 将old_dir的第i行第11列数据写入到new_dir第j行第11列
        # else:
        #     pass
        newWb.save(new_dir)
        # doc.close()

    # 复制文件到指定路径
    def file_copy(self, rm_file):
        rm_file_dir = 'E:\\load_bi\\' + self.str_day + '\\' + rm_file
        new_file_dir = 'C:\\fakepath\\' + rm_file
        if os.path.isfile(new_file_dir):
            os.remove(new_file_dir)
        shutil.copyfile(rm_file_dir, new_file_dir)

    # 从Aftp复制400溢出.xlsx 和 潜客推荐.xlsx 5096.xls 到日期文件
    def file_copy_two(self):
        file_list = ('400溢出.xlsx', '潜客推荐.xlsx', '5096.xls')
        for file in file_list:
            rm_file_dir1 = 'E:\\Aftp\\ftpput\\' + file
            new_file_dir1 = 'E:\\load_bi\\' + self.str_day + '\\' + file
            if os.path.isfile(new_file_dir1):
                os.remove(new_file_dir1)
            shutil.copyfile(rm_file_dir1, new_file_dir1)


if __name__ == '__main__':
    # @version : 3.4
    # @Author  : robot_lei
    # @Software: PyCharm Community Edition
    # @Features: 芒果汽车有限公司内部用于处理excel模板脚本
    # 将这三个脚本合并成一张
    str_day = str(datetime.date.today()).replace('-', '')
    log_path = 'E:\\load_bi\\' + str_day + '\\log.log'
    logging.basicConfig(filename=log_path)
    try:
        excel_cp().file_copy_two()
        old_file_name_s = ('降价通知.xls', '车库线索.xls', '400溢出.xlsx',
                           '潜客推荐.xlsx', '详情页未登录线索.xls', '分期工具.xls', '首页弹窗.xls',
                           '微信小程序.xls', '预约看车.xls', '询价.xls')
        leads_source_str = ('r510', 'r520', 'r880', 'r722', 'r995', 'r994', 'r993', 'r992', 'r991', 'r990')
        new_file_name = '5096.xls'
        for old_file_name in old_file_name_s:
            size = os.path.getsize('E:\\load_bi\\' + str_day + '\\' + old_file_name)
            if size > 0:
                excel_cp().excel_merge(old_file_name, new_file_name)
        # 把家速贷的数据追加复制到 5096.xls
        # os.system("python excel_copy_jiasudai.py")

        # 复制文件到指定路径
        excel_cp().file_copy(new_file_name)
    except Exception as e:
        s = traceback.format_exc()
        print(e)
        tra = traceback.print_exc()
        # print(tra)
