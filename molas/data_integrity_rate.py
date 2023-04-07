import json
import os,sys
import pandas as pd
from pandas import read_csv
from pathlib import Path
import datetime
from config import cfg
from log import LOGGER


def setting_cols_name(charset,lidarheights):
    #默认雷达有的字段
    # lidar_dic =  cfg.get_lidar_list()

    if charset == 'utf-8':
        cols = ['Date', 'Timestamp', 'Longitude', 'Latitude', 'Height', 'ROLL', 'PITCH', 'HEADING', 'ROLL_IMU',
                'PITCH_IMU', 'Azimuth', 'Wiper Count']
        #通过配置文件加的字段
        # heights = cfg.get_lidar_height()
        for height in lidarheights:
            cols.append('{}m CNR'.format(height))
            cols.append('{}m iRWS(m/s)'.format(height))
            cols.append('{}m DataType'.format(height))
            cols.append('{}m Horizontal Wind Speed(m/s)'.format(height))
            cols.append('{}m Horizontal Wind Direction(°)'.format(height))
            cols.append('{}m X-Direction Wind Speed(m/s)'.format(height))
            cols.append('{}m Y-Direction Wind Speed(m/s)'.format(height))
            cols.append('{}m Z-Direction Wind Speed(m/s)'.format(height))
        # print(cols)
        return cols
    elif charset == 'gbk':
        cols = ['年月日', '时间戳', '经度', '纬度', '高度', 'ROLL', 'PITCH', 'HEADING', 'ROLL_IMU',
                'PITCH_IMU', '方位角', '温度','雨刮器计数']
        # 通过配置文件加的字段
        # heights = cfg.get_lidar_height()
        for height in lidarheights:
            cols.append('{}m信噪比(dB)'.format(height))
            cols.append('{}m视向风速(m/s)'.format(height))
            cols.append('{}m数据类型'.format(height))
            cols.append('{}m水平风速(m/s)'.format(height))
            cols.append('{}m水平风向(°)'.format(height))
            cols.append('{}mx方向风速(m/s)'.format(height))
            cols.append('{}my方向风速(m/s)'.format(height))
            cols.append('{}mz方向风速(m/s)'.format(height))
        # print(cols)
        return cols
#返回csv字段列表

#读取文件的函数，可能没考虑乱码的情况，不确定产生乱码导致程序崩溃
def read_molas_data(filepath,charset,lidarheights, header=9):
    fpath = Path(filepath)

    cols_name = setting_cols_name(charset,lidarheights)
    #
    if os.path.exists(fpath):
        if charset == 'utf-8':
            raw_data = read_csv(fpath, header=header, sep='\t', encoding='utf-8', on_bad_lines='skip', index_col=False)
            raw_data = raw_data[cols_name]
            raw_data['Time and Date'] = pd.to_datetime(raw_data['Date'] + raw_data['Timestamp'])
            raw_data.set_index('Time and Date', inplace=True)
            # print(raw_data)
            return raw_data
        elif charset == 'gbk':
            raw_data = read_csv(fpath, header=header, sep='\t', encoding='gbk',on_bad_lines='skip', index_col=False)
            raw_data = raw_data[cols_name]
            raw_data['Time and Date'] = pd.to_datetime(raw_data['年月日'] + raw_data['时间戳'])
            raw_data.set_index('Time and Date', inplace=True)
            return raw_data

    else:
        LOGGER.error("Reading Molas file(%s) failed!" % filepath)
        LOGGER.error("Reading Molas lidarheights(%s) failed!" % lidarheights)
        return None

# 匹配风速，风向，等完整率
#针对雷达输出是中文的情况：
def statistical_integrity_rate_gbk(df, heights, freq='24H'):
    availability_col_1 = []
    for height in heights:
        availability_col_1.append('1-s Data Availability at {}.0m'.format(height))
    return_df = pd.DataFrame()
    for height in heights:

        try:
            if not df.empty:
                count_number1 = df.resample(freq).count()
                return_df[''.join([col for col in availability_col_1 if ("at " + str(height)) in col])] = \
                    count_number1['{}m水平风速(m/s)'.format(height)].apply(lambda x: (x / 86400 * 100))

                return_df[''.join([col for col in availability_col_1 if ("at " + str(height)) in col])] = return_df[
                    ''.join([col for col in availability_col_1 if ("at " + str(height)) in col])].apply(
                    lambda x: 100.00 if x > 100 else round(x, 2))
        except:
            return_df = pd.DataFrame()
    print(return_df)
    return return_df
#针对雷达输出是英文的情况：
def statistical_integrity_rate_utf_8(df, heights, freq='24H'):
    availability_col_1 = []
    for height in heights:
        availability_col_1.append('1-s Data Availability at {}.0m'.format(height))
    return_df = pd.DataFrame()
    for height in heights:
        try:
            if not df.empty:
                count_number1 = df.resample(freq).count()
                return_df[''.join([col for col in availability_col_1 if ("at " + str(height)) in col])] = \
                    count_number1['{}m Horizontal Wind Speed(m/s)'.format(height)].apply(lambda x: (x / 86400 * 100))

                return_df[''.join([col for col in availability_col_1 if ("at " + str(height)) in col])] = return_df[
                    ''.join([col for col in availability_col_1 if ("at " + str(height)) in col])].apply(
                    lambda x: 100.00 if x > 100 else round(x, 2))
        except:
            return_df = pd.DataFrame()
    print(return_df)
    return return_df

def integrity_rate_run():
    if len(sys.argv) > 1:
        input_date = sys.argv[1]
        yes = input_date
    else:
        now = datetime.datetime.now()
        yes = now + datetime.timedelta(days=-1)
        yes = yes.strftime('%Y%m%d')
    #读取配置文件
    lidar_dic = cfg.get_lidar_list()
    lidar1heights = lidar_dic["lidar_1"]["Lidar_heights"]
    lidar2heights = lidar_dic["lidar_2"]["Lidar_heights"]
    #判断雷达2是否安装，根据配置文件不同
    if lidar_dic['lidar_2']['installed'] == 0:
        #根据配置文件获取完整的雷达文件路径名字
        lidar_path_2 = lidar_dic['lidar_2']['path'] + lidar_dic['lidar_2']['prefix'] + yes + lidar_dic['lidar_2'][
            'suffix']
        lidar2charset = lidar_dic["lidar_2"]["Lidar_charset"]  # set charset
        df2 = read_molas_data(lidar_path_2,lidar2charset,lidar2heights)
    else:
        lidar2charset=None
        df2 = pd.DataFrame()
    # 判断雷达1是否安装
    if lidar_dic['lidar_1']['installed'] == 0:
        # 根据配置文件获取完整的雷达文件路径名字
        lidar_path_1 = lidar_dic['lidar_1']['path'] + lidar_dic['lidar_1']['prefix'] + yes + lidar_dic['lidar_1'][
            'suffix']
        lidar1charset = lidar_dic["lidar_1"]["Lidar_charset"]  # set charset
        df1 = read_molas_data(lidar_path_1,lidar1charset,lidar1heights)
    else:
        lidar1charset=None
        df1 = pd.DataFrame()
    #获取雷达高度
    # print(lidar1heights)
    # print(lidar2heights)
    # 外层分别对出现的集中情况做一个判断，去调用相应处理gbK和utf-8的函数
    if lidar1charset == "gbk":
        result1 = statistical_integrity_rate_gbk(df1, lidar1heights, freq='24H')
    elif lidar1charset == "utf-8":
        result1 = statistical_integrity_rate_utf_8(df1, lidar1heights, freq='24H')
    else:
        result1 = None
    if lidar2charset == "gbk":
        result2 = statistical_integrity_rate_gbk(df2, lidar2heights, freq='24H')
    elif lidar2charset == "utf-8":
        result2 = statistical_integrity_rate_utf_8(df2, lidar2heights, freq='24H')
    else:
        result2 = None

    columns1 = []
    if result1 is not None:
        for index, row in result1.items():
            columns1.append(index)
        # print('columns1:', columns1)
    columns2 = []
    if result2 is not None:
        for index, row in result2.items():
            columns2.append(index)
        # print('columns2:', columns2)
    Lidar1 = {}
    Lidar2 = {}
#获取雷达1高度值；如果一个雷达文件没有的情况考虑进去
    for i in range(0, len(lidar1heights)):
        height1 = str(lidar1heights[i])
        if columns1:
            column_1 = str(round(float(result1[columns1[i]].values[0]), 2))
            key = column_1.split('.')[-1]
            if key == '00':
                column_1 = column_1.split('.')[0]

            key1 = {f"{height1}": column_1}

            Lidar1.update(key1)
    for j in range(0,len(lidar2heights)):
        height2 = str(lidar2heights[j])
        if columns2:
            column_2 = str(round(float(result2[columns2[j]].values[0]), 2))
            key = column_2.split('.')[-1]
            if key == '00':
                column_2 = column_2.split('.')[0]

            key2 = {f"{height2}": column_2}
            Lidar2.update(key2)

    if Lidar1:
        lidar1 = json.dumps(Lidar1, separators=(',', ':'))
        lidar1 = "{Lidar1:" + lidar1 + "}"
    else:
        lidar1 = "{Lidar1:-1}"

    if Lidar2:
        lidar2 = json.dumps(Lidar2, separators=(',', ':'))
        lidar2 = ",Lidar2:" + lidar2 + '}'
    else:
        lidar2 = ",Lidar2:-1}"

        # 拼接字符串
    data = "MolasAV:" + lidar1 + lidar2
    print(lidar1,'\n',lidar2)
    return lidar1 ,lidar2

if __name__ == '__main__':

    integrity_rate_run()

