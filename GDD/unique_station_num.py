import pandas as pd
import os

# 文件夹路径
folder_path = './temp_data'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查是否为CSV文件
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # 使用pandas读取CSV文件
        df = pd.read_csv(file_path, dtype={'气象站名称': str}, low_memory=False)

        # 计算'气象站名称'列中唯一值的数量
        unique_station_count = df['气象站名称'].nunique()

        # 打印每个文件的唯一气象站名称数量
        print(f'File: {filename} has {unique_station_count} unique station names.')
