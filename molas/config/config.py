# coding=utf-8

import json


class Config:
    def __init__(self, cfg_file="cfg.json"):
        self.__cfg_file = cfg_file
        f = open(cfg_file, encoding='utf-8')
        self.decoded_cfg = json.loads(f.read())
        f.close()

    def save(self):
        with open(self.__cfg_file, 'w', encoding='utf-8') as f:
            json.dump(self.decoded_cfg, f, indent=4)

    def get_version(self):
        return self.decoded_cfg['version']

    def get_name(self):
        return self.decoded_cfg['device_name']

    def get_root_dir(self):
        return self.decoded_cfg['root_dir']

    def get_lidar1_configuration(self):
        installed = self.decoded_cfg['lidar_configuration']["lidar1_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_lidar2_configuration(self):
        installed = self.decoded_cfg['lidar_configuration']["lidar2_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_lidar1_type(self):
        return self.decoded_cfg['lidar_configuration']["lidar1_type"]

    def get_lidar2_type(self):
        return self.decoded_cfg['lidar_configuration']["lidar2_type"]

    def get_lidar1_path(self):
        return self.decoded_cfg['lidar_configuration']["lidar1_path"]

    def get_lidar2_path(self):
        return self.decoded_cfg['lidar_configuration']["lidar2_path"]

    def get_weather_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["weather_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_trimble_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["trimble_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_trimble_ip_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["trimble_ip_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_trimble_bk_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["trimble_bk_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_current_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["current_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_wave_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["wave_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_valimeter_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["valimeter_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_ct_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["ct_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_cti_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["cti_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_modbus_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["modbus_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_system_is_installed(self):
        installed = self.decoded_cfg['sensor_configuration']["system_is_installed"]
        if installed == 0:
            return True
        else:
            return False

    def get_trimble_path(self):
        return self.decoded_cfg['sensor_configuration']["trimble_path"]

    def get_trimble_bk_path(self):
        return self.decoded_cfg['sensor_configuration']["trimble_bk_path"]

    def get_trimble_ip_path(self):
        return self.decoded_cfg['sensor_configuration']["trimble_ip_path"]

    def get_weather_path(self):
        return self.decoded_cfg['sensor_configuration']["weather_path"]

    def get_current_path(self):
        return self.decoded_cfg['sensor_configuration']["current_path"]

    def get_wave_path(self):
        return self.decoded_cfg['sensor_configuration']["wave_path"]

    def get_valimeter_path(self):
        return self.decoded_cfg['sensor_configuration']["valimeter_path"]

    def get_ct_path(self):
        return self.decoded_cfg['sensor_configuration']["ct_path"]

    def get_cti_path(self):
        return self.decoded_cfg['sensor_configuration']["cti_path"]

    def get_modbus_path(self):
        return self.decoded_cfg['sensor_configuration']["modbus_path"]

    def get_system_path(self):
        return self.decoded_cfg['sensor_configuration']["system_path"]




    def get_lidar_height(self):
        return self.decoded_cfg['Lidar_height']

    def get_lidar_list(self):
        return self.decoded_cfg['lidar_data']


    def get_ping_cfg(self):
        return self.decoded_cfg['ping_cfg']

    def get_ip_prefix(self):
        return self.decoded_cfg['ip_prefix']

    def get_all_devices(self):
        return self.decoded_cfg['devices']



    def get_all_plc_info(self):
        return self.decoded_cfg['plc_info']

    def get_plc_port(self):
        return self.decoded_cfg['plc_info']['port']

    def get_plc_site(self):
        return self.decoded_cfg['plc_info']['site']

    def get_plc_query_addr(self):
        return self.decoded_cfg['plc_info']['query_addr']

    def get_fuelfull_installed(self):
        return self.decoded_cfg['fuelfull_is_installed']





if __name__ == '__main__':
    cfg = Config()
