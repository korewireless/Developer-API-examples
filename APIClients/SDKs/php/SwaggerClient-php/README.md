# PHP library for the ClientsAPI-Production
The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.

## Overview
This API client can be used to generate an API for Client Management services in the Developer Portal. Project Details:

- API version: 1.0.0

## Requirements

PHP 5.5 and later

## Installation & Usage
### Composer

To install the bindings via [Composer](http://getcomposer.org/), add the following to `composer.json`:

```
{
  "repositories": [
    {
      "type": "git",
      "url": "https://github.com/git_user_id/git_repo_id.git"
    }
  ],
  "require": {
    "git_user_id/git_repo_id": "*@dev"
  }
}
```

Then run `composer install`

### Manual Installation

Download the files and include `autoload.php`:

```php
    require_once('/path/to/SwaggerClient-php/vendor/autoload.php');
```

## Tests

To run the unit tests:

```
composer install
./vendor/bin/phpunit
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');

// Configure API key authorization: LambdaTokenAuthorizer
$config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKey('Unused', 'YOUR_API_KEY');
// Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
// $config = Swagger\Client\Configuration::getDefaultConfiguration()->setApiKeyPrefix('Unused', 'Bearer');
// Configure API key authorization: api_key
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

## Documentation for API Endpoints

All URIs are relative to *https://client.api.korewireless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**getPingStatus**](docs/Api/DefaultApi.md#getpingstatus) | **GET** /v1/ping | 
*DefaultApi* | [**v1PingOptions**](docs/Api/DefaultApi.md#v1pingoptions) | **OPTIONS** /v1/ping | 

## Documentation For Models

 - [Error](docs/Model/Error.md)

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



