# Python library for the ClientsAPI-Production
The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.

## Overview
This API client can be used to generate an API for Client Management services in the Developer Portal. Project Details:

- API version: 1.0.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: LambdaTokenAuthorizer
configuration = swagger_client.Configuration()
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Unused'] = 'Bearer'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_mock_response_id = 'x_mock_response_id_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.get_ping_status(x_mock_response_id=x_mock_response_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->get_ping_status: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
x_mock_response_id = 'x_mock_response_id_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.v1_ping_options(x_mock_response_id=x_mock_response_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_ping_options: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://client.api.korewireless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_ping_status**](docs/DefaultApi.md#get_ping_status) | **GET** /v1/ping | 
*DefaultApi* | [**v1_ping_options**](docs/DefaultApi.md#v1_ping_options) | **OPTIONS** /v1/ping | 

## Documentation For Models

 - [Error](docs/Error.md)

## Documentation For Authorization


## LambdaTokenAuthorizer

- **Type**: API key
- **API key parameter name**: Unused
- **Location**: HTTP header

## api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Author


