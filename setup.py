from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requiremnts(file_path:str)->List[str]:
    '''
    this function return the list of requirements 
    '''
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace("\n","") for req in requiremnts ]
        
        if HYPEN_E_DOT in requiremnts:
            requiremnts.remove(HYPEN_E_DOT) 

    return requiremnts


setup(
name ='mlproject',
version='0.0.1',
author='Shubham',
author_email='shubhamkondewar98@gmail.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn']
install_requires=get_requiremnts('requirements.txt')
)
