# get_ocorrencias_api_rio


1. To build the deploy and schedule it to run every 20 minutes, run the following line:
prefect deploy .base/functions.py:ocorrencias_workflow --interval 1200        ##Building the deploy with interval schedule   
##Set deployment name: etl-deploy
##Set process (local) infrastructure
##Set work pool name: etl-worker

2. To iniciate the job, run the following line:
prefect worker start --pool etl-worker                                        ##Iniciating the flow
