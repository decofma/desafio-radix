from ..base.insere_db       import InsertDb as insere_db
from ..base.consulta_db     import QueryDb  as consulta_db
from ..base                 import dao_base as base
import pandas               as pd

class SensorDao(base.RadixDB):
    def __init__(self) -> None:
        super().__init__

    def upload_sensor_data(self, param_data: dict):
        nome_rotina = 'upload sensor data dao'
        try:
            query = insere_db().insert_sensor_data()
            paramsDb = {
                "equipmentId" : param_data['equipmentId'],
                "timestamp" : param_data['timestamp'],
                "value" : param_data['value']
            }

            dataframe = pd.readsql(sql= query, con=super().get_connection(), params=paramsDb)
            return super().convert_dataframe_to_dict(dataframe)
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
        
    def get_avg_sensor_day(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data dao'
        try:
            query = consulta_db().get_sensor_data_avg_day()
            dataframe = pd.readsql(sql= query, con=super().get_connection())
            return super().convert_dataframe_to_dict(dataframe)
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
    def get_avg_sensor_twodays(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data dao'
        try:
            query = consulta_db().get_sensor_data_avg_twodays()
            dataframe = pd.readsql(sql= query, con=super().get_connection())
            return super().convert_dataframe_to_dict(dataframe)
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
    def get_avg_sensor_week(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data dao'
        try:
            query = consulta_db().get_sensor_data_avg_week()
            dataframe = pd.readsql(sql= query, con=super().get_connection())
            return super().convert_dataframe_to_dict(dataframe)
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro
    def get_avg_sensor_month(self, param_data: dict):
        nome_rotina = 'obter valor medio sensor data dao'
        try:
            query = consulta_db().get_sensor_data_avg_month()
            dataframe = pd.readsql(sql= query, con=super().get_connection())
            return super().convert_dataframe_to_dict(dataframe)
        
        except Exception as erro:
            print(__file__)
            print('funcao:',nome_rotina)
            print('erro:', erro)
            return erro