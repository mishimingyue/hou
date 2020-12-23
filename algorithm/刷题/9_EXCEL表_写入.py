# -*- coding:utf-8 -*-
import xlwt

title = ['1', '2', '3', '4']
stus = [['mary', 20, '5', 89.9]]
# 新建一个excel对象
wbk = xlwt.Workbook()
# 添加一个名为 课程表的sheet页
sheet = wbk.add_sheet('stu')
for i in range(len(title)):  # 写入表头
    sheet.write(0, i, title[i])  # 写入每行,第一个值是行，第二个值是列，第三个是写入的值
for i in range(len(stus)):
    if i != 0:  # 如果不是表头的话
        for j in range(4):
            sheet.write(i, j, stus[i][j])  # 循环写入每行数据
# 保存数据到‘test.xls’文件中
wbk.save("C:\\app\python\\xing_1.xls")  # 保存excel必须使用后缀名是.xls的，不是能是.xlsx的
