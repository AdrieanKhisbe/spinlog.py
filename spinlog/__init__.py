#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Spinlog is here to assist you write progress of your script
    It's a wrapper on halo and fallback to logging
    in case of non interactive script
"""

__version__ = "0.1.0"
from .core import LogProgress
