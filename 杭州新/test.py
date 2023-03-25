import pandas as pd
import os

# 获取当前目录下所有 .xlsx 文件的文件名
file_names = [f for f in os.listdir('.') if f.endswith('.xls')]


# 定义要提取的列的列名
col_names = [7, 8]

# 新建一个空的 DataFrame，用于存放提取出来的数据
result_df = pd.DataFrame(columns=col_names)

# 遍历每个 Excel 文件，读取指定的两列，并添加到 result_df 中
for file_name in file_names:
    df = pd.read_excel(file_name, usecols=col_names)
    print(df.columns)

    result_df = pd.concat([result_df, df])

# 将结果保存为新的 Excel 文件
result_df.to_excel('last_result.xlsx', index=False)


#
# import pandas as pd
# import os
#
# # 获取当前目录下所有 .xls 文件的文件名
# file_names = [f for f in os.listdir('.') if f.endswith('.xls')]
#
# # 定义要提取的列的列名
# col_names = ['年份', '单位名称']
#
# # 新建一个空的 DataFrame，用于存放提取出来的数据
# result_df = pd.DataFrame(columns=col_names)
#
# # 遍历每个 Excel 文件，读取指定的两列，并添加到 result_df 中
# for file_name in file_names:
#     df = pd.read_excel(file_name, usecols=col_names)
#     result_df = pd.concat([result_df, df])
#
# # 使用 groupby() 方法按照年份对数据进行分组
# groups = result_df.groupby('年份')
#
# # 遍历每个分组，将其保存到以该年份命名的 Excel 文件中
# for year, group in groups:
#     group.to_excel(f'{year}.xlsx', index=False)
