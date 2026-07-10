from setuptools import setup

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().split()

setup(
    name='embedded_model',
    version='1.0',
    packages=['embedded_model'],
    package_dir={'embedded_model': '.'},
    url='',
    license='',
    author='OCTO',
    author_email='',
    description='Package embedded-model pour les TP de la formation industrialisation de la data science avancée',
    install_requires=requirements
)
