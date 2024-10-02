```py
# 工作簿--workbook
# 表单-sheet
# 单元格-cell
# 行:row
# 列:col
import xlrd  
# 打开一个 Excel 文件  
workbook = xlrd.open_workbook('文件路径.xls')  
# 获取所有工作表的名称  
sheet_names = workbook.sheet_names()  
# 通过索引或名称获取工作表  
sheet1 = workbook.sheet_by_index(0)  # 通过索引获取第一个工作表  
# 读取单元格数据  
cell_value = sheet1.cell_value(rowx=0, colx=0)  # 读取第一行第一列的数据
# 读取行数
rows = sheet1.nrows 
# 读取列数
cols = sheet1.ncols
# 读取行元素(整行元素)
sheet1.row_value(i)
# 读取列元素
sheet1.col_values(j)

在python中，定义字符串s,s[-1]表示最后一个字符
```
```py
import xlrd

# 读取excel步骤
# 1.打开一个工作簿
work_book = xlrd.open_workbook('计科2班成员.xls')
# 2.获取sheet表单(第一个)
sheet1 = work_book.sheet_by_index(0)  # sheet1
# 3.通过sheet表单进行按行或者按列读取
# 按行读取
rows = sheet1.nrows  # 读取行数
# print(rows) # 34
'''
for i in range(rows):
    print(sheet_first.row_values(i))  # 34*2
'''
# 按列读取
cols = sheet1.ncols  # 读取列数
# print(cols) # 2
'''
for j in range(cols):
    print(sheet_first.col_values(j))  # 2*34
'''
for i in range(rows):
    cell = sheet1.cell_value(i, 1)
    # 判断学号尾号是否为1，4，7
    if cell[-1] in {'1', '4', '7'}:
        print(sheet1.cell_value(i, 0))
```

