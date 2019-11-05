"""setup.py"""

from setuptools import setup

setup(name='techcookbook', 
    version='0.1',
    description='TechCookBook Python Packge', 
    url='https://techcookbook.com', 
    author='@yuki', 
    author_email='', 
    license='MIT', 
    packages=['techcookbook'],
    install_requires=
    [
        'PyMySQL'
    ],      
    zip_safe=False)
