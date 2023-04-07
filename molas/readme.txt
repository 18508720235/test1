一、配置cfg.json
lidar_1：
· 更改Lidar_charset为对应的雷达的输出格式；例：gbk或utf-8
· 更改Lidar_heights为对应雷达的输出高度(可以为不同高度，和雷达匹配)
· 更改prefix配置，为对应雷达编号和型号
lidar_2：
· 更改Lidar_charset为对应的雷达的输出格式；例：utf-8或gbk
· 更改Lidar_heights为对应雷达的输出高度(可以为不同高度，和雷达匹配)
· 更改prefix配置，为对应雷达编号和型号
二、调用integrity_rate_run()，返回lidar1和lidar的前一天的各个高度的完整率信息
 解析对应的lidar完整率信息。通过sent_message调用send.py发送出去

使用：将run_intergrity_send.bat添加到计划任务中 。或者执行生成昨天的完整率以及告警文件有无生成