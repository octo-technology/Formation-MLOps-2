# Formation Industrialisation d'un projet de data science avancée

## How do I install it

First, make sure you have miniconda or anaconda installed. If not, install it!

Create a conda env

```sh
conda create -n python_indus_avancee python=3.8
conda activate python_indus_avancee
```

Retrieve project from gitlab

Start a jupyter notebook in the folder

```sh
cd formation_indus_ds
jupyter-notebook
```

If your `python_indus_avancee` environment is not available in `jupyter` interface (when clicking on new). You should :

- Quit jupyter-notebook with <kbd>ctrl</kbd>+<kbd>c</kbd> in terminal
- Run `conda install -n python_indus_avancee nb_conda_kernels`
- Start `jupyter-notebook`

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