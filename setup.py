from setuptools import setup, find_packages

setup(
    name="bfscan",
    version='0.0.1',
    packages=find_packages(),
    author="Thiago Pereira de Oliveira Carvalho, Frederico Schmitt Kremer",
    author_email="thg.baum@gmail.com, fred.s.kremer@gmail.com",
    description="bfscan is designed to detect foodborne pathogens using bloom filter",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    keywords="bioinformatics bloom filter data science foodborne pathogen",
    entry_points = {'console_scripts':[
     
        ]},
    install_requires = [
        requirement.strip('\n') for requirement in open("requirements.txt")
    ]
)
