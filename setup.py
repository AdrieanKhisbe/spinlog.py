#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages

with open('spinlog/.version') as f:
    version = f.read()
 
setup(
    name='spinlog',
    version=version,
    packages=["spinlog"],
    author="AdrieanKhisbe",
    author_email="adriean.khisbe@live.fr",
    description="Spinner Logger for Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=["halo"],
    include_package_data=True,
    url='http://github.com/AdrieanKhisbe/spinlog.py',
    keywords="cli terminal log logger logging shell update animation progress",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Logging",
    ],
)
