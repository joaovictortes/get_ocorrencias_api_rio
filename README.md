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
         | to_csv            |		--------------------> LOAD
         +-------------------+

**get_ocorrencias:** extracts data as json by making a request to the API endpoint "ocorrencias_abertas" and retrieves open occurrences.

**get_atividades:** iterates over each **eventoId** obtained from the previous step and consume the API on endpoint "ocorrencias_orgaos_responsaveis" to retrieve activity data for each ocurrence.

**to_dataframe:** selects only activities from "CET-RIO", converts the list with the data into a pandas dataframe, append some columns from both API endpoints, export to csv.

**remove_duplicates:** import the recently saved csv, remove its duplicates and overwrite it.


**RUNNING INSTRUCTIONS:**

**Install all packages listed on requirements.txt**

**Download functions.py from the repository to a local base directory**

**Build the deploy and schedule it to run every 20 minutes:**

`prefect deploy .base/functions.py:ocorrencias_workflow --interval 1200`

Set deployment name: **etl-deploy**

Set **process** (local) infrastructure

Set work pool name: **etl-worker**  

prefect.yaml file contains pre-configured parameters to deploy.

**Initiate the job:**

`prefect worker start --pool etl-worker`

The file dados_eventos.csv will be created in the base directory.
