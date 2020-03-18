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

{'version': '1.2.1'}
```

or to take advantage of comparing and checking for bad versions, you
can use the following form

```python
import etelemetry
etelemetry.check_available_version("nipy/nipype", "1.5.0")

{'version': '1.2.1'}
```