## Etelemetry-client

[![Build Status](https://travis-ci.org/sensein/etelemetry-client.svg?branch=master)](https://travis-ci.org/sensein/etelemetry-client)
[![codecov](https://codecov.io/gh/sensein/etelemetry-client/branch/master/graph/badge.svg)](https://codecov.io/gh/sensein/etelemetry-client)

A lightweight python client to communicate with the etelemetry server

### Installation

```
pip install etelemetry
```

### Usage

```python
import etelemetry
etelemetry.get_project("nipy/nipype")

{'version': '1.4.2', 'bad_versions': ['1.2.1', '1.2.3', '1.3.0']}
```

or to take advantage of comparing and checking for bad versions, you
can use the following form

```python
import etelemetry
etelemetry.check_available_version("nipy/nipype", "1.2.1")

A newer version (1.4.2) of nipy/nipype is available. You are using 1.2.1
You are using a version of nipy/nipype with a critical bug. Please use a different version.
returns: {'version': '1.4.2', 'bad_versions': ['1.2.1', '1.2.3', '1.3.0']}
```