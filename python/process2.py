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
