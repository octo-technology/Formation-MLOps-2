from setuptools import setup, find_packages

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().split()

setup(
    name='formation_indus_ds_avancee',
    version='1.0',
    packages=["indus"],
    package_dir={"indus": "formation_indus_ds_avancee"},
    url='',
    license='',
    author='Octo-LENA-ISMA',
    author_email='',
    description='Demonstration pour la formation indus de la data science avancee',
    install_requires=requirements
)
