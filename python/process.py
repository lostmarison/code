import pandas as pd

# 输入待处理文件地址
input_file_path = 'D:\\class\\计科学生信息.xlsx'
# 读取
df = pd.read_excel(input_file_path, sheet_name='Sheet1')
# 目标班级：计科2班
target_class = 2322107012
# 筛选出计科2班学生信息
new_df = df[df.iloc[:, 5] == target_class]
# 需要的列：姓名（第4列）、学号（第5列）、寝室（第2列）、床位（第3列）
required = new_df.iloc[:, [3, 4, 1, 2]]
# 重命名列以匹配所需的表头
required.columns = ['姓名', '学号', '寝室', '床位']
# 输出文件地址
output_file_path = 'D:\\class\\计科2班学生信息.xlsx'
# index=False:不将DataFrame的索引（行标签）写入到输出的Excel文件中
'''
required.to_excel(output_file_path, index=False)
'''
