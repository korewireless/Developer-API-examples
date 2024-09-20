# ClientsApiProduction.DefaultApi

All URIs are relative to *https://client.api.korewireless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPingStatus**](DefaultApi.md#getPingStatus) | **GET** /v1/ping | 
[**v1PingOptions**](DefaultApi.md#v1PingOptions) | **OPTIONS** /v1/ping | 

<a name="getPingStatus"></a>
# **getPingStatus**
> getPingStatus(opts)



### Example
```javascript
import {ClientsApiProduction} from 'clients_api_production';
let defaultClient = ClientsApiProduction.ApiClient.instance;

// Configure API key authorization: LambdaTokenAuthorizer
let LambdaTokenAuthorizer = defaultClient.authentications['LambdaTokenAuthorizer'];
LambdaTokenAuthorizer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//LambdaTokenAuthorizer.apiKeyPrefix = 'Token';

// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ClientsApiProduction.DefaultApi();
let opts = { 
  'xMockResponseId': "xMockResponseId_example", // String | 
  'authorization': "authorization_example" // String | 
};
apiInstance.getPingStatus(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMockResponseId** | **String**|  | [optional] 
 **authorization** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[LambdaTokenAuthorizer](../README.md#LambdaTokenAuthorizer), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="v1PingOptions"></a>
# **v1PingOptions**
> v1PingOptions(opts)



### Example
```javascript
import {ClientsApiProduction} from 'clients_api_production';

let apiInstance = new ClientsApiProduction.DefaultApi();
let opts = { 
  'xMockResponseId': "xMockResponseId_example", // String | 
  'authorization': "authorization_example" // String | 
};
apiInstance.v1PingOptions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMockResponseId** | **String**|  | [optional] 
 **authorization** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

