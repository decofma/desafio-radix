class RadixDB():
    def __init__(self) -> None:
        """ METODO CONSTRUTOR DA CLASSE BASE DO DAO PARA DEFINIÇÃO DO BANCO DE DADOS"""
        DB_BASE = "NOME DO BANCO"
        DB_PASS = "SENHA DO BANCO"
        DB_HOST = "HOST DO BANCO"
        super().__init__(DB_BASE, DB_PASS, DB_HOST)