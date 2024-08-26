# responsible to building my application as a package for distribution purpose
from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file__path:str)->List[str]:
    '''
    This function will take as parameter a file path in string format and is expected to return a List of strings(return type hint),
    it is just giving information not actually enforcing return (->List[str])
    '''
    requirements=[]
    with open(file__path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n',"") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

    '''
    Purpose: The open() function is used to open the file at the path specified by file__path.
    Using with: The with statement ensures that the file is properly closed after the block of code is executed, 
    even if an error occurs.
    Reading Lines: file_obj.readlines() reads all lines in the file and returns them as a list of strings.
    Each string corresponds to a line in the file, including the newline character (\n) at the end of each line.
    Assignment: The list of lines is assigned to the requirements variable.

    req.replace -> This line is intended to remove newline characters (\n) from each string in the requirements list.
    '''

# it has metadata information about the entire project
setup(
    name='ml_end_to_end_project', # giving the name of the project
    version='0.0.1' ,# giving the initial vcersion that will be built
    author='Subrat Bahuguna',
    author_email='bahuguna.subrat211996@gmail.com',
    packages=find_packages(), #inbuilt lib+ to find the packages automatically, it will check in how many packages __init__.py is running
    install_requires=get_requirements('requirements.txt')
   ## intall_requires=['pandas','numpy','seaborn'] -> when lot of libraries required to be installed it's not feasible
)

