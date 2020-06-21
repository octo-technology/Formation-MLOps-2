from setuptools import setup

with open('requirements.txt', 'r') as requirements_file:
    requirements = requirements_file.read().split()

setup(
    name='exposing_predictions',
    version='1.0',
    packages=['exposing_predictions'],
    package_dir={'exposing_predictions': '.'},
    url='',
    license='',
    author='OCTO',
    author_email='',
    description='Package exposing-predictions pour les TP de la formation industrialisation de la data science avancée',
    install_requires=requirements
)
