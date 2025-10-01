#Filename:	setup.py
#Author:	Wang Yongjie
#Email:		yongjie.wang@ntu.edu.sg
#Date:		Min 29 Nov 2020 05:34:04  WIB

from setuptools import setup, find_packages

setup(
    author = 'wang yongjie',
    author_email = 'yongjie.wang@ntu.edu.sg',
    description = 'The package for counterfactual explanations on Pytorch platform',
    keyowrk  = 'counterfactual explantions, pytorch, recourse',
    url = 'https://github.com/wangyongjie-ntu/Counterfactual-Explanations-Pytorch',
    project_url = { 
        "Documentation": "https://counterfactual-explanations-pytorch.readthedocs.io/en/main/",
        "Code": "https://github.com/wangyongjie-ntu/Counterfactual-Explanations-Pytorch",
        },  

    classifiers = [ 
        'License::OSI Approved::Python Software Foundation License'
    ],  
    name = 'counterfactual_explanations',
    package = find_packages(),
    #package_data = {'wang':['data/test.txt']},
    #py_modules = ['module1', 'module2'],
    version='0.1.0',
    #install_requires=[
    #    'pyjokes > 0.5'
    #],  
    extras_require={
     'interactive': ['matplotlib >= 2.2.0', 'jupyter']
     },  
    
)            
