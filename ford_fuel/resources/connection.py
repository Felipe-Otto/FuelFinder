import json
import os
from google.cloud import bigquery

key_path = 'fordfuel-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
client = bigquery.Client()
table_id = 'ford.Posto'

# Defina o esquema da tabela explicitamente
schema = [
    bigquery.SchemaField('idPosto', 'INTEGER'),
    bigquery.SchemaField('NomePosto', 'STRING'),
    bigquery.SchemaField('Rua', 'STRING'),
    bigquery.SchemaField('Bairro', 'STRING'),
    bigquery.SchemaField('Cidade', 'STRING'),
    bigquery.SchemaField('Estado', 'STRING'),
    bigquery.SchemaField('CEP', 'STRING'),
    bigquery.SchemaField('Latitude', 'STRING'),
    bigquery.SchemaField('Longitude', 'STRING'),
]

def enviar_dados_para_bigquery(data):
    id = selecionar_id()
    rows_to_insert = [{
        'idPosto': id,
        'NomePosto': data['Nome Posto'],
        'Rua': data['Rua'],
        'Bairro': data['Bairro'],
        'Cidade': data['Cidade'],
        'Estado': data['Estado'],
        'CEP': data['CEP'],
        'Latitude': data['latitude'],
        'Longitude': data['longitude'],
    }]

    # Insira os dados diretamente na tabela "Posto"
    errors = client.insert_rows_json(table_id, rows_to_insert)

    if errors:
        return f'Erro: {errors}'
    else:
        return 'Dados enviados para o BigQuery com sucesso!'


def selecionar_id():
    query = f'SELECT MAX(idPosto) AS max_idPosto FROM `ford.Posto` '

    # Execute a consulta
    query_job = client.query(query)

    # Obtenha os resultados da consulta
    results = query_job.result()

    # Inicialize uma lista vazia para armazenar os resultados serializáveis
    serialized_results = []

    # Itere pelos resultados (deve haver apenas um)
    for row in results:
        max_idPosto = row.max_idPosto
        # Converta o valor para um tipo serializável, como int
        serialized_result = {'max_idPosto': int(max_idPosto)}
        serialized_results.append(serialized_result)

    return int(serialized_results[0]["max_idPosto"]) + 1

