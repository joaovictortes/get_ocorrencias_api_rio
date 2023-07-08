import requests
import pandas as pd
import json
import numpy as np
from prefect import flow, task

# Passo 1: Consumir API de eventos
@task(name="get_ocorrencias")
def get_ocorrencias():
    try:
        url_eventos = "https://api.dados.rio/v2/adm_cor_comando/ocorrencias_abertas/"
        response_eventos = requests.get(url_eventos)
        ocorrencias_abertas = response_eventos.json()
        return ocorrencias_abertas
    except:
        print("Erro: ", response_eventos.status_code)


# Passo 2: Iterar sobre cada id de evento e consumir API de atividades
@task(name="get_atividades")
def get_atividades(ocorrencias_abertas):
    lista_atividades = []
    try:
        for evento in ocorrencias_abertas['eventos']:
            evento_id = evento['id']
            url_acoes = f"https://api.dados.rio/v2/adm_cor_comando/ocorrencias_orgaos_responsaveis?eventoId={evento_id}"
            response_acoes = requests.get(url_acoes, timeout=5)
            ocorrencias_orgaos_responsaveis = response_acoes.json()
            
            try:  
                # Passo 3: Append dados de atividades em uma lista
                for atividade in ocorrencias_orgaos_responsaveis['atividades']:
                    lista_atividades.append({
                        "id": evento["id"],
                        "inicio": evento["inicio"],
                        "titulo": evento["titulo"],
                        "descricao": atividade["descricao"],
                        "status": atividade["status"],
                        "orgao": atividade["orgao"],
                        #"quantidade_ocorrencia": atividade["quantidade_ocorrencia"]
                    })   
            except:
                print("Erro no parseamento do json")
    except:
        print("Erro no Request da API: ", response_acoes.status_code)
    return lista_atividades

# Passo 4: Filtrar as ações da CET-RIO, gerar e dar o append no csv.    
@task(name="to_dataframe")
def to_dataframe(lista_atividades):
    df = pd.DataFrame(lista_atividades, columns=["id", "inicio", "titulo", "descricao", "status", "orgao"])
    df = df[df['orgao'] == 'CET-RIO']
    df.sort_values(by=['inicio'], inplace=True)
    df.to_csv("dados_eventos.csv", index=False, mode='a', header=False)

@task(name="remove_duplicates")
def remove_duplicates():
    df = pd.read_csv('dados_eventos.csv')
    df = df.drop_duplicates(keep='last')
    df.to_csv("dados_eventos.csv", index=False)
    
    
@flow
def ocorrencias_workflow():
    ocorrencias_abertas = get_ocorrencias()
    lista_atividades = get_atividades(ocorrencias_abertas)
    to_dataframe(lista_atividades)
    remove_duplicates()

if __name__ == "__main__":
    ocorrencias_workflow()