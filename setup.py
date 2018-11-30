# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 00:23:29 2018

@author: laptopTCC
"""

from setuptools import setup, find_packages
from distutils.extension import Extension
# import versioneer

DISTNAME = 'FirstPackagePython'
INSTALL_REQUIRES = (
    ['pandas>=0.19.2', 'requests>=2.3.0', 'wrapt', 'lxml']
)

VERSION = '0.0'
LICENSE = 'BSD'
DESCRIPTION = 'My First Package'
AUTHOR = "KhanhPhamDinh"
EMAIL = "phamdinhkhanh.tkt53.neu@gmail.com"
URL = "https://github.com/phamdinhkhanh/FirstPackagePython"
DOWNLOAD_URL = ''

setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=EMAIL,
      url=URL,
      packages=find_packages(include = ['FirstPackagePython', 'FirstPackagePython.*'],
                             exclude=['config', 'description', 'HEAD']),
      package_dir = {'FirstPackagePython':'src'} ,
      package_data={'FirstPackagePython': ['template/*.txt', 'template/*.rst']},
      py_modules = ['src.sum', 'src.mul'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Trader/Investor/Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
      ],
      keywords = 'data',
      install_requires=INSTALL_REQUIRES,
      test_suite='tests',
      zip_safe=False,
     )