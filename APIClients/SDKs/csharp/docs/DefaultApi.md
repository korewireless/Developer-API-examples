# IO.Swagger.Api.DefaultApi

All URIs are relative to *https://client.api.korewireless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetPingStatus**](DefaultApi.md#getpingstatus) | **GET** /v1/ping | 
[**V1PingOptions**](DefaultApi.md#v1pingoptions) | **OPTIONS** /v1/ping | 

<a name="getpingstatus"></a>
# **GetPingStatus**
> void GetPingStatus (string xMockResponseId = null, string authorization = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class GetPingStatusExample
    {
        public void main()
        {
            // Configure API key authorization: LambdaTokenAuthorizer
            Configuration.Default.AddApiKey("Unused", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("Unused", "Bearer");
            // Configure API key authorization: api_key
            Configuration.Default.AddApiKey("x-api-key", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.AddApiKeyPrefix("x-api-key", "Bearer");

            var apiInstance = new DefaultApi();
            var xMockResponseId = xMockResponseId_example;  // string |  (optional) 
            var authorization = authorization_example;  // string |  (optional) 

            try
            {
                apiInstance.GetPingStatus(xMockResponseId, authorization);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.GetPingStatus: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMockResponseId** | **string**|  | [optional] 
 **authorization** | **string**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[LambdaTokenAuthorizer](../README.md#LambdaTokenAuthorizer), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="v1pingoptions"></a>
# **V1PingOptions**
> void V1PingOptions (string xMockResponseId = null, string authorization = null)



### Example
```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class V1PingOptionsExample
    {
        public void main()
        {
            var apiInstance = new DefaultApi();
            var xMockResponseId = xMockResponseId_example;  // string |  (optional) 
            var authorization = authorization_example;  // string |  (optional) 

            try
            {
                apiInstance.V1PingOptions(xMockResponseId, authorization);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling DefaultApi.V1PingOptions: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xMockResponseId** | **string**|  | [optional] 
 **authorization** | **string**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
