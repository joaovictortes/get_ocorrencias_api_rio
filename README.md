# get_ocorrencias_api_rio


Run the following command to build the deploy and schedule it to run every 20 minutes:

prefect deploy .base/<file.py>:<flow name> --interval <interval between runs>
prefect deploy .base/functions.py:ocorrencias_workflow --interval 1200
