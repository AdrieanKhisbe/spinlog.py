#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
import spinlog


with open('spinlog/.version') as f:
    version = f.read()
 
setup(
    name='spinlog',
    version=version,
    packages=find_packages(),
    author="AdrieanKhisbe",
    author_email="adriean.khisbe@live.fr",
    description="Spinner Logger for Python",
    long_description=open('README.md').read(),
    install_requires=["halo"],
    include_package_data=True,
    url='http://github.com/AdrieanKhisbe/spinlog.py',
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Logging",
    ],
)
