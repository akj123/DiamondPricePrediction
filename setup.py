from setuptools import find_packages , setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]: ### This mean that filepath is in string format and the return type is list of strings

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n' , '') for req in requirements]

        if HYPEN_E_DOT in requirements:  ## We do not need this to be executed as it will call setup.py
            requirements.remove(HYPEN_E_DOT)


        return requirements

setup(

    name = 'DiamondPricePrediction' ,
    version = '0.0.1' ,
    author = 'ankit' ,
    author_email = 'ankitj53@gmail.com',
    install_requires = get_requirements('requirements.txt') ,  ### This includes all the installed packages ; directly taking from the requirements.txt
    packages= find_packages()

)