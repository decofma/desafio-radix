@echo off

set FLASK_ENV = development
set PORT = 'NUMERO DA PORTA ONDE O FRONTEND ESTARA RODANDO'
set FLASK_DEBUG = True
set APP = radix_challenge.app:create_app
set RADIX_DB_USERNAME = 'NOME DO OWNER DO BANCO'
set RADIX_DB_PASS = 'SENHA BANCO' 
set RADIX_DB_HOST = 'NOME DO BANCO'

flask run -p %PORT%