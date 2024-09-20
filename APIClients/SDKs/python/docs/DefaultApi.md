# swagger_client.DefaultApi

All URIs are relative to *https://client.api.korewireless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ping_status**](DefaultApi.md#get_ping_status) | **GET** /v1/ping | 
[**v1_ping_options**](DefaultApi.md#v1_ping_options) | **OPTIONS** /v1/ping | 

# **get_ping_status**
> get_ping_status(x_mock_response_id=x_mock_response_id, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: LambdaTokenAuthorizer
configuration = swagger_client.Configuration()
configuration.api_key['Unused'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Unused'] = 'Bearer'
# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = 'YOUR_API_KEY'
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_mock_response_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[LambdaTokenAuthorizer](../README.md#LambdaTokenAuthorizer), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ping_options**
> v1_ping_options(x_mock_response_id=x_mock_response_id, authorization=authorization)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
x_mock_response_id = 'x_mock_response_id_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)

try:
    api_instance.v1_ping_options(x_mock_response_id=x_mock_response_id, authorization=authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->v1_ping_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_mock_response_id** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

