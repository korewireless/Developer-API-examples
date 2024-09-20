# DefaultApi

All URIs are relative to *https://client.api.korewireless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPingStatus**](DefaultApi.md#getPingStatus) | **GET** /v1/ping | 
[**v1PingOptions**](DefaultApi.md#v1PingOptions) | **OPTIONS** /v1/ping | 

<a name="getPingStatus"></a>
# **getPingStatus**
> getPingStatus(xMockResponseId, authorization)



### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.DefaultApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();

// Configure API key authorization: LambdaTokenAuthorizer
ApiKeyAuth LambdaTokenAuthorizer = (ApiKeyAuth) defaultClient.getAuthentication("LambdaTokenAuthorizer");
LambdaTokenAuthorizer.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//LambdaTokenAuthorizer.setApiKeyPrefix("Token");

// Configure API key authorization: api_key
ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
api_key.setApiKey("YOUR API KEY");
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.setApiKeyPrefix("Token");

DefaultApi apiInstance = new DefaultApi();
String xMockResponseId = "xMockResponseId_example"; // String | 
String authorization = "authorization_example"; // String | 
try {
    apiInstance.getPingStatus(xMockResponseId, authorization);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#getPingStatus");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMockResponseId** | **String**|  | [optional]
 **authorization** | **String**|  | [optional]

### Return type

null (empty response body)

### Authorization

[LambdaTokenAuthorizer](../README.md#LambdaTokenAuthorizer)[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="v1PingOptions"></a>
# **v1PingOptions**
> v1PingOptions(xMockResponseId, authorization)



### Example
```java
// Import classes:
//import io.swagger.client.ApiException;
//import io.swagger.client.api.DefaultApi;


DefaultApi apiInstance = new DefaultApi();
String xMockResponseId = "xMockResponseId_example"; // String | 
String authorization = "authorization_example"; // String | 
try {
    apiInstance.v1PingOptions(xMockResponseId, authorization);
} catch (ApiException e) {
    System.err.println("Exception when calling DefaultApi#v1PingOptions");
    e.printStackTrace();
}
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

