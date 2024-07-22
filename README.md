
# desafio-radix

Sistema responsável por receber dados dos sensores de oleo e gás e salvar no banco de dados
## Requisitos

- Python 3.9.x
- Docker (opcional, para execução em container)
## Documentação da Aplicação - Desafio Radix

#### Sumário

- Descrição do Código

- Instalação e Execução

- Endpoints da API

- Testes

### Estrutura do Código

| Arquivo | Descrição |
| ------ | ------ |
| App.py | Configura e inicializa a aplicação Flask com suporte a CORS. |
| root_blueprint.py | Define e inicializa o blueprint principal da aplicação, configurando as rotas e a documentação da API.|
| sensor_api.py | Define as rotas e os modelos para manipulação dos dados dos sensores.|
| sensor_facade.py | Implementa a lógica de negócio da aplicação, intermediando as requisições entre a API e o DAO.|
| sensor_dao.py | Acesso aos dados no banco de dados, realizando as operações de inserção e consulta.|
| consulta_db.py | Contém as queries SQL para consultar os dados dos sensores.|
| insere_db.py | Contém a query SQL para inserir dados dos sensores no banco de dados. |
| dao_base.py | Classe base para definição do banco de dados. |
| test_endpoints.py | Teste unitário para verificar os endpoints da API. |


### Instalação

Para rodar essa aplicação siga o passo a passo abaixo:

Instalação e Execução

```bash
  python -m venv .venv
  call .venv\Scripts\activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  call .\radix_challenge\run_dsv.bat
```

### Endpoints da API

#### POST /insert-sensor-data
Insere dados de sensores.

Request Body
json
Copiar código
```
{
    "equipmentId": "string",
    "timestamp": "date",
    "value": "float"
}
```
##### Response
- 200 OK: Dados inseridos com sucesso.
- 400 Bad Request: Falha no carregamento dos dados.

#### POST /upload-csv

Carrega dados de sensores a partir de um arquivo CSV.

Request Body
Arquivo CSV com colunas: equipmentId, timestamp, value.

##### Response
- 200 OK: Dados carregados com sucesso.
- 400 Bad Request: Falha no carregamento dos dados.

#### GET /get-avg-sensor-data-day
Obtém a média dos dados dos sensores do último dia.

##### Response
- 200 OK: Dados retornados com sucesso.
- 400 Bad Request: Falha no retorno dos dados.

#### GET /get-avg-sensor-data-two-days
Obtém a média dos dados dos sensores dos últimos dois dias.

##### Response
- 200 OK: Dados retornados com sucesso.
- 400 Bad Request: Falha no retorno dos dados.

#### GET /get-avg-sensor-data-week
Obtém a média dos dados dos sensores da última semana.

##### Response
- 200 OK: Dados retornados com sucesso.
- 400 Bad Request: Falha no retorno dos dados.

#### GET /get-avg-sensor-data-month
Obtém a média dos dados dos sensores do último mês.

#### Response
- 200 OK: Dados retornados com sucesso.
- 400 Bad Request: Falha no retorno dos dados.

### Testes

#### Explicação dos Testes
- test_insert_sensor_data_success: Testa a inserção de dados do sensor com sucesso.
- test_insert_sensor_data_failure: Testa a falha na inserção de dados do sensor com dados ausentes.
- test_upload_sensor_data_csv_success: Testa o upload de dados de sensores a partir de um arquivo CSV.
- test_get_avg_sensor_data_day_success: Testa a obtenção da média dos dados dos sensores do último dia.
- test_get_avg_sensor_data_two_days_success: Testa a obtenção da média dos dados dos sensores dos últimos dois dias.
- test_get_avg_sensor_data_week_success: Testa a obtenção da média dos dados dos sensores da última semana.
- test_get_avg_sensor_data_month_success: Testa a obtenção da média dos dados dos sensores do último mês.

Para rodar os testes unitários, execute:

```bash
python -m unittest discover -s radix_challenge/test -p 'test_endpoints.py'
```