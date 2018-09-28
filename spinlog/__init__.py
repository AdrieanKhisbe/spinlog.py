#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Spinlog is here to assist you write progress of your script
    It's a wrapper on halo and fallback to logging
    in case of non interactive script
"""
from os.path import join, dirname
with open(join(dirname(__file__), '.version')) as f:
    __version__ = f.read()

from .core import Spinner
