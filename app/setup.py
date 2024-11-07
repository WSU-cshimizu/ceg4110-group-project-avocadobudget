
from setuptools import setup 

  
setup( 
    name='dbOperations', 
    version='0.1', 
    description='Crud Operations', 
    author='Daniel Cronauer', 
    author_email='dcronauer@gmail.com', 
    packages=['dbOperations', 'expenseClass'], 
    install_requires=[ 
        'flask', 
        'sqlite3',
        'plotly'
    ], 
) 
