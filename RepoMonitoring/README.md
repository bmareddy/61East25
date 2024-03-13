# RepoMonitoring

This codebase does the following:
* Allow users to see the number of stars and forks on a given GitHub repository. 
 * `python stars_and_forks.py` to see the output
* Create an Airflow DAG that runs once every day, and alerts if there have been more than 10000 _new_ stars

## Developer Notes
* `repo.py` contains the collection of classes
 * `RepoPlatform` standardizes the platform and api url relationship
 * `Repo` is a parent class that will allow extending this to any type of platform
 * `GitHub` contains the core logic that was requested as part of this requirement
* `monitor.py` is Airflow based DAG so may not be runnable unless you have local Airflow or is deployed to manager service such as MWAA