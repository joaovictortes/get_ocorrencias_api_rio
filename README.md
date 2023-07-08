# get_ocorrencias_api_rio


Prefect config:
prefect deployment build .src/functions.py:ocorrencias_worfklow --name rio-api
prefect deployment apply ocorrencias_worfklow-deployment.yaml
