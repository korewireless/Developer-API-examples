# Swagger\Client\DefaultApi

All URIs are relative to *https://client.api.korewireless.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPingStatus**](DefaultApi.md#getpingstatus) | **GET** /v1/ping | 
[**v1PingOptions**](DefaultApi.md#v1pingoptions) | **OPTIONS** /v1/ping | 

# **getPingStatus**
> getPingStatus($x_mock_response_id, $authorization)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure API key authorization: LambdaTokenAuthorizer
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Unused', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Unused', 'Bearer');// Configure API key authorization: api_key
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('x-api-key', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('x-api-key', 'Bearer');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$x_mock_response_id = "x_mock_response_id_example"; // string | 
$authorization = "authorization_example"; // string | 

try {
    $apiInstance->getPingStatus($x_mock_response_id, $authorization);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->getPingStatus: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_mock_response_id** | **string**|  | [optional]
 **authorization** | **string**|  | [optional]

### Return type

void (empty response body)

### Authorization

[LambdaTokenAuthorizer](../../README.md#LambdaTokenAuthorizer), [api_key](../../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **v1PingOptions**
> v1PingOptions($x_mock_response_id, $authorization)



### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

$apiInstance = new Swagger\Client\Api\DefaultApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$x_mock_response_id = "x_mock_response_id_example"; // string | 
$authorization = "authorization_example"; // string | 

try {
    $apiInstance->v1PingOptions($x_mock_response_id, $authorization);
} catch (Exception $e) {
    echo 'Exception when calling DefaultApi->v1PingOptions: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_mock_response_id** | **string**|  | [optional]
 **authorization** | **string**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

