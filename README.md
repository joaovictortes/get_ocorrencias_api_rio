# get_ocorrencias_api_rio


Run the following commands to build the deploy and schedule it to run every 20 minutes:

prefect deploy .base/functions.py:ocorrencias_workflow --interval 1200        ##Building the deploy with interval schedule   
##Set deployment name: etl-deploy
##Set process (local) infrastructure
##Set work pool name: etl-worker
prefect worker start --pool etl-worker                                        ##Iniciating the flow
