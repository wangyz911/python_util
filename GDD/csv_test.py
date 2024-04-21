import pandas as pd
import os

# 文件夹路径
folder_path = 'D:\BaiduNetdiskDownload\\1929～2023 年 GSOD 气象站点数据\\1929～2023 年 GSOD 气象站点数据\分年数据'
new_folder_path = './temp_data/'
# 您想要筛选的特定Station代码
specific_station_code = '57083099999'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 检查是否为CSV文件
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)

        # 使用pandas读取CSV文件
        df = pd.read_csv(file_path, dtype={'气象站名称': str}, low_memory=False)
        # 在应用.str.endswith()之前，用空字符串填充NA/NaN值
        filtered_data = df[df['气象站名称'].fillna('').str.endswith(', CH')]
        # # 筛选出特定观测站的所有记录
        # filtered_data = df[df['气象站名称'] == specific_station_code]

        # 检查筛选到的数据量
        data_count = len(filtered_data)
        if data_count > 0:
            # 数据量大于0，写入新的CSV文件
            new_file_name = filename.replace('年GSOD气象站点数据.csv', '_GSOD_Station_Data_china.csv')
            new_file_path = os.path.join(new_folder_path, new_file_name)
            filtered_data.to_csv(new_file_path, index=False)
            print(f'{data_count} records found and written to {new_file_path}')
        else:
            # 数据量为0，打印警告
            print(f'Warning: No data found for Station {specific_station_code} in {filename}. No file created.')

