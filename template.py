'''Template for Creating the folder structure'''

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') #to save Logging informations 


project_name = "cnnClassifier" #Template Name Standard

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurtaion.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


] #defining the List of files to be created 

for filepath in list_of_files:
    filepath = Path(filepath) #returns file path
    filedir, filename = os.path.split(filepath) #splts the file directory and file




    if filedir !='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating Directory: {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):    
        with open(filepath,'w')as f:
            pass
            logging.info(f"Creating Empty file : {filepath}")


    else:
        logging.info(f"{filename} already exist")