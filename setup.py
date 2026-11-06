from setuptools import find_packages,setup 
from typing import List 


def get_requirements()->list[str]:
    """
    This function will return list of requirements

    """ 
    requirements_lst:List[str] = []

    try: 
        with open('requirements.txt',"r") as file:
            # read lines from the file
            lines = file.readlines() 
            # process each line 
            for line in lines: 
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirements_lst.append(requirement)
               
    except FileNotFoundError:
        print("requirements.txt file not found") 

    return requirements_lst


setup(
    name="Network Security", 
    version="0.0.1",
    author="BajrangJaiswal01",
    author_email="Siteshjaisujaiswal@gmail.com",
    packages=find_packages() ,
    install_requires=get_requirements()

)