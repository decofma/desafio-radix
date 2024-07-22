def get_dict_endpoint(tipo_retorno: str, msg_retorno: str, dado_retorno: dict) -> dict:
    return {
        "resposta_server" : {
            "tipo_retorno"  : tipo_retorno.lower(),
            "msg_retorno"   : msg_retorno
        },
        "dado_retornado"    : dado_retorno 
    }

def convert_csv_to_dict(equipmentId: str , timestamp: any , value: float) -> dict:
    return {
        "equipmentId"   : equipmentId,
        "timestamp"     : timestamp, 
        "value"         : value
    }