import requests
import time
import datetime
import os,sys
import json
from logger import logger
from datetime import datetime, timedelta
from data_integrity_rate import integrity_rate_run
from config import cfg
def send_request(message):
    #url_head = 'http://127.0.0.1:5007/send_urgent/JzmL2020/1/1/1/'
    #message = bytes(message, 'utf-8')
    #message = message.hex()
    #url_tail = message
    b=message.encode('ascii') 
    os.system('python send.py 1 %s' % b.hex())
    #url = url_head + url_tail
    #print('send_msg:', url)
    #logger.info(url)
    #requests.get(url)
if __name__ == "__main__":
    diff_days = 1
    yesterday = datetime.now() - timedelta(days=diff_days)
    date_day = yesterday.strftime('%Y%m%d')
    lidar_dic = cfg.get_lidar_list()
    lidar1_prefix = lidar_dic['lidar_1']['prefix']
    lidar2_prefix = lidar_dic['lidar_2']['prefix']
    fpath_1 = 'D:\\ba\\data\\lidar\\molas51\\' + lidar1_prefix + str(date_day) + '.txt'
    fpath_2 = 'D:\\ba\\data\\lidar\\molas52\\' + lidar2_prefix + str(date_day) + '.txt'

    print(fpath_1)
    print(fpath_2)
    lidar1_av, lidar2_av = integrity_rate_run()
    if os.path.exists(fpath_1):

        print("lidar1_av:",lidar1_av)
        send_request(lidar1_av)
        logger.info(lidar1_av)
        time.sleep(15)
    else:
        message ='the %s not exist'%fpath_1
        print(message)
        send_request(message)
        logger.warning(message)
        time.sleep(15)
        
    if os.path.exists(fpath_2):
        print("lidar2_av:",lidar2_av)
        send_request(lidar2_av)
        logger.info(lidar2_av)
        time.sleep(15)
    else:
        message = 'the %s not exist' % fpath_2
        print(message)
        send_request(message)
        logger.warning(message)
        time.sleep(15)






