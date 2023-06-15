from setuptools import setup

with open('requirements.txt', 'r') as requirements_file:
    requirements = [requirement for requirement in requirements_file.read().split('\n') if
                    not requirement.startswith('# ')]

with open('requirements_test.txt', 'r') as requirements_file:
    test_requirements = requirements_file.read().split()

setup(
    name='formation_indus_ds_avancee',
    version='1.2',
    packages=['formation_indus_ds_avancee'],
    package_dir={'formation_indus_ds_avancee': 'formation_indus_ds_avancee'},
    url='',
    license='',
    author='OCTO',
    author_email='',
    description='Package pour le TP de la formation industrialisation de la data science avancée',
    install_requires=requirements,
    tests_require=test_requirements
)
