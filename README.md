## Etelemetry-client

[![Build Status](https://travis-ci.org/mgxd/etelemetry-client.svg?branch=master)](https://travis-ci.org/mgxd/etelemetry-client)
[![codecov](https://codecov.io/gh/mgxd/etelemetry-client/branch/master/graph/badge.svg)](https://codecov.io/gh/mgxd/etelemetry-client)

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
