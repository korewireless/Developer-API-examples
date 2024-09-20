# {{classname}}

All URIs are relative to *https://client.api.korewireless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetPingStatus**](DefaultApi.md#GetPingStatus) | **Get** /v1/ping | 
[**V1PingOptions**](DefaultApi.md#V1PingOptions) | **Options** /v1/ping | 

# **GetPingStatus**
> GetPingStatus(ctx, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DefaultApiGetPingStatusOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiGetPingStatusOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMockResponseId** | **optional.String**|  | 
 **authorization** | **optional.String**|  | 

### Return type

 (empty response body)

### Authorization

[LambdaTokenAuthorizer](../README.md#LambdaTokenAuthorizer), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **V1PingOptions**
> V1PingOptions(ctx, optional)


### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
 **optional** | ***DefaultApiV1PingOptionsOpts** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a pointer to a DefaultApiV1PingOptionsOpts struct
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMockResponseId** | **optional.String**|  | 
 **authorization** | **optional.String**|  | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

