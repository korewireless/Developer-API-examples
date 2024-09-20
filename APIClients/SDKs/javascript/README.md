# JavaScript library for the ClientsAPI-Production

ClientsApiProduction - JavaScript client for clients_api_production
The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.

## Overview
This API client can be used to generate an API for Client Management services in the Developer Portal. Project Details:

- API version: 1.0.0
- Package version: 1.0.0
- Add "type": "module", in package.json
- Convert 'require' to 'import' to read files and add js extension in all js files in the import, if needed.

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install clients_api_production --save
```

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var ClientsApiProduction = require('clients_api_production');
var defaultClient = ClientsApiProduction.ApiClient.instance;

// Configure API key authorization: LambdaTokenAuthorizer
var LambdaTokenAuthorizer = defaultClient.authentications['LambdaTokenAuthorizer'];
LambdaTokenAuthorizer.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//LambdaTokenAuthorizer.apiKeyPrefix['Unused'] = "Token"

// Configure API key authorization: api_key
var api_key = defaultClient.authentications['api_key'];
api_key.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix['x-api-key'] = "Token"

var api = new ClientsApiProduction.DefaultApi()
var opts = { 
  'xMockResponseId': "xMockResponseId_example", // {String} 
  'authorization': "authorization_example" // {String} 
};
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
};
api.getPingStatus(opts, callback);
```

## Documentation for API Endpoints

All URIs are relative to *https://client.api.korewireless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ClientsApiProduction.DefaultApi* | [**getPingStatus**](docs/DefaultApi.md#getPingStatus) | **GET** /v1/ping | 
*ClientsApiProduction.DefaultApi* | [**v1PingOptions**](docs/DefaultApi.md#v1PingOptions) | **OPTIONS** /v1/ping | 

## Documentation for Models

 - [ClientsApiProduction.Error](docs/Error.md)

## Documentation for Authorization


### LambdaTokenAuthorizer

- **Type**: API key
- **API key parameter name**: Unused
- **Location**: HTTP header

### api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

