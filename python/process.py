'''
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
'''
import xlrd


class Student:
    def __init__(self, filename, sheet_index):
        # 私有属性，用于存储工作簿和工作表
        self.__workbook = xlrd.open_workbook(filename)  # 1.打开一个工作簿
        self.__sheet = self.__workbook.sheet_by_index(sheet_index)  # 2.获取sheet表单

    def find_last_number(self, *nums):
        rows = self.__sheet.nrows  # 读取行数
        for i in range(rows):
            cell = self.__sheet.cell_value(i, 1)
            for num in nums:
                # 判断学号尾号是否在nums中
                if cell[-1] == num:
                    name = self.__sheet.cell_value(i, 0)
                    print(name)

    def find_student_information(self, student_name):
        rows = self.__sheet.nrows
        for i in range(rows):
            name = self.__sheet.cell_value(i, 3)
            if student_name == name:
                dorm = int(self.__sheet.cell_value(i, 1))
                student_id = int(self.__sheet.cell_value(i, 4))
                print("寝室:%d 学号:%d" % (dorm, student_id))


finder1 = Student('计科2班成员.xls', 0)
finder1.find_last_number('1', '4', '7')
