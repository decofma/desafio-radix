from ...model.dao.sensor_dao import SensorDao as sensor_d

class SensorFacade():
    def __init__(self) -> None:
        super().__init__

    def upload_sensor_data(self, param_data: dict):
        nome_rotina = 'upload sensor data facade'
        try:
            data = sensor_d.upload_sensor_data(param_data)
            return data
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
        
    def get_avg_sensor_day(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data facade'
        try:
            data = sensor_d.get_avg_sensor_day(param_data)
            return data
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
    def get_avg_sensor_twodays(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data facade'
        try:
            data = sensor_d.get_avg_sensor_twodays(param_data)
            return data
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
    def get_avg_sensor_week(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data facade'
        try:
            data = sensor_d.get_avg_sensor_week(param_data)
            return data
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
    def get_avg_sensor_month(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data facade'
        try:
            data = sensor_d.get_avg_sensor_month(param_data)
            return data
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
