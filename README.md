This Python data workflow performs a series of steps to extract data from Rio de Janeiro APIs, transform it, and load it into a CSV file. The workflow consists of the following functions/tasks:

         +-------------------+
         | get_ocorrencias   |		--------------------> EXTRACT
         +----------+--------+
                   |
                   v
         +-------------------+
         | get_atividades    |		--------------------> EXTRACT
         +----------+--------+
                   |
                   v
         +-------------------+
         | to_dataframe      |		--------------------> TRANSFORM
         +----------+--------+
                   |
                   v
         +-------------------+
         | remove_duplicates |		------------------> TRANSFORM
         +----------+--------+
                   |
                   v
         +-------------------+
         | to_csv           		|		--------------------> LOAD
         +-------------------+

**get_ocorrencias:** extracts data as json by making a request to an API and retrieving open occurrences.

**get_atividades:** extracts data by iterating over each **eventoId** obtained from the previous step and consuming "atividades" API to retrieve activity data for each event.

**to_dataframe:** converts the list with the extracted data into a pandas dataframe. It structures and prepares the data for further processing.

**remove_duplicates:** transforms the df by removing any duplicate entries, ensuring data integrity.

**to_csv:** loads the transformed data into a CSV file. It writes the DataFrame to a CSV file.


**RUNNING INSTRUCTIONS:**


**Build the deploy and schedule it to run every 20 minutes:**

`prefect deploy .base/functions.py:ocorrencias_workflow --interval 1200`

Set deployment name: **etl-deploy**

Set **process** (local) infrastructure

Set work pool name: **etl-worker**

**Initiate the job:** 

prefect.yaml file contains pre-configured parameters to deploy.

`prefect worker start --pool etl-worker`
