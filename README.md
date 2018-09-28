# spinlog.py

[![PyPI](https://img.shields.io/pypi/v/spinlog.svg)](https://pypi.org/project/spinlog/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/spinlog.svg)](https://pypi.python.org/pypi/spinlog)
[![Build Status](https://travis-ci.org/AdrieanKhisbe/spinlog.py.svg?branch=master)](https://travis-ci.org/AdrieanKhisbe/spinlog.py)
[![codecov](https://codecov.io/gh/AdrieanKhisbe/spinlog.py/branch/master/graph/badge.svg)](https://codecov.io/gh/AdrieanKhisbe/spinlog.py)

> Spinner Logger for Python

## Installation

Just `pip install spinlog` and you can use it.

## Usage

Spinlog is build on top of [halo](https://github.com/manrajgrover/halo) providing a different API
to interact with the spinner.

### Basic Usage
```python
from spinlog import Spinner
from time import sleep

print("About to launch Spinner")
with Spinner.get("I'm spinning around") as s:
    sleep(2)
    s.info("Here is an info message while spinning around")
    # you can use s.warn, s.error, or s.debug
    sleep(2)
print("Spinning Over")
```

### Advanced usage
Spinlog is build in such a manner that you can disable the spinning animation
and replace it with proper logging without having to change the codebase.

This is done by creating a spinner instance, potentialy configured with two logger,
the `concommitant_logger` to be run alongside the spinner (for logging to file for instance),
and the `alternative_logger` to replace spinner animation and logging.

A complete example can be found in [the examples folder](./examples/with_logger.py)
Here is an except:
```python
# imports and logger definitions
should_spin = "--no-spin" not in sys.argv
# Configure spinner
spinner = Spinner(spinner="triangle", is_spinning=should_spin,
                  alternative_logger=stream_logger, concommitant_logger=file_logger)
# Use spinner
with spinner("Operation in progress") as s:
    sleep(2)
    s.info("Checkpoint reached")
    sleep(2)
```

## Licence
MIT © [AdrieanKhisbe](https://github.com/AdrieanKhisbe)
