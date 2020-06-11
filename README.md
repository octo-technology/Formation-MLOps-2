# Formation Industrialisation d'un projet de data science avancée

## How do I install it

First, make sure you have miniconda or anaconda installed. If not, install it!

Create a conda env

```bash
make conda-env
conda activate python_indus_avancee
```

Use the DAG Airflow 

export AIRFLOW_HOME= {path}/dsind2

# install from pypi using pip
pip install apache-airflow

# initialize the database
airflow initdb

# start the web server, default port is 8080
airflow webserver -p 8080

# start the scheduler
airflow scheduler


Retrieve project from gitlab

## How to follow it

It is highly linked to the presentation of the formation.

To navigate between steps change branch.

To see all branches

```sh
git branch -a
```

To start the practical work you should checkout branch `0_initial_state`

```sh
git checkout 0_initial_state
```

## For windows users

You will need a `git bash` terminal and a conda terminal :

- All `git` commands should be executed in the `git bash` terminal.
- All `python` and `conda` related commands should be executed in the conda terminal.

## For linux users

Every command can be executed in your terminal.
