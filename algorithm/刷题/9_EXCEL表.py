# -*- coding:utf-8 -*-
import xlrd

# 打开excel
wb = xlrd.open_workbook(r"C:\app\python\111.xls")  # 打开的这个excel必须存在，否则会报错
# 获取所有sheet页的名字
print(wb.sheet_names())
# 按名字查找第二张表单
# sheet=wb.sheet_by_name('abc2')#根据sheet页的名字获取sheet页
sheet = wb.sheet_by_index(2)  # 根据sheet页的索引获取sheet页
# 获取sheet页的行数和列数
print(sheet.nrows)
print(sheet.ncols)
# 打印每行信息
for rownum in range(sheet.nrows):  # 循环取每行的数据
    print(sheet.row_values(rownum))  # 取每行的数据
# 按照索引打印对应单元格内容
# print sheet.cell(1,1).value
cell_A2 = sheet.cell(0, 1).value  # 获取指定单元格的值，第一个值是列，第二个值是行
print(cell_A2)
