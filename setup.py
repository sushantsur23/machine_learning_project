from setuptools import setup, find_packages
from typing import List


#Declaring variables for setup function
NAME = 'Housing-Predictor'
VERSION = '0.0.1'
AUTHOR = 'Sushant Sur'
DESCRIPTION = "THIS PROJECT IS ON HOUSE PRICE PREDICTION"
PACKAGES = ['housing']
REQUIREMENT_FILE_NAME = 'requirements.txt'
HYPHEN_E_DOT = "-e ."

def get_requirements_list()-> List[str]:
    """Returns a list of requirements as per requirements.txt file
        Going to return a list which will contain name of all libraries as updated. 
    """    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
        # requirement_list = [requirement_list.replace("\n", "\n)]

setup(
name = NAME,
version = VERSION,
author = AUTHOR,
description = DESCRIPTION,
packages = find_packages(),         #siumilar to using PACKAGES
install_requires = get_requirements_list(),
)
