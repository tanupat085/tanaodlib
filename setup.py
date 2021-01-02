﻿import io
from os.path import abspath, dirname, join
from setuptools import find_packages, setup


HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.rst'
])

setup(
  name = 'tanaod',      
  packages = ['tanaod'], 
  version = '0.0.2',  
  license='MIT', 
  description = 'First libary from tanaod',
  long_description=DESCRIPTION,
  author = 'tanaod',                 
  author_email = 'tanupat085@gmail.com',     
  url = 'https://github.com/tanupat085/tanaodlib',  
  download_url = 'https://github.com/tanupat085/tanaodlib/archive/v0.0.2.zip',  
  keywords = ['tanaod', 'oop', 'Tanupat Satitvattana'],   
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Education',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)