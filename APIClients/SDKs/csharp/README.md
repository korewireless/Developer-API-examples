# C# library for the ClientsAPI-Production

The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.

## Overview
This API client can be used to generate an API for Client Management services in the Developer Portal. Project Details:

- API version: 1.0.0
- SDK version: 1.0.0
- Comment request.AddFile(param.Value.Name, param.Value.Writer, param.Value.FileName, param.Value.ContentType); in ApiClient.cs file
- Remove the line <OutputType>Library</OutputType> from IO.Swagger.csproj file

<a name="frameworks-supported"></a>
## Frameworks supported
- .NET 4.0 or later
- Windows Phone 7.1 (Mango)

<a name="dependencies"></a>
## Dependencies
- [RestSharp](https://www.nuget.org/packages/RestSharp) - 110.2.0 or later
- [Json.NET](https://www.nuget.org/packages/Newtonsoft.Json/) - 7.0.0 or later
- [JsonSubTypes](https://www.nuget.org/packages/JsonSubTypes/) - 1.2.0 or later

The DLLs included in the package may not be the latest version. We recommend using [NuGet](https://docs.nuget.org/consume/installing-nuget) to obtain the latest version of the packages:
```
Install-Package RestSharp
Install-Package the older version of the RestSharp NuGet package (<=106.15)
Install-Package Newtonsoft.Json
Install-Package JsonSubTypes
```

NOTE: RestSharp versions greater than 105.1.0 have a bug which causes file uploads to fail. See [RestSharp#742](https://github.com/restsharp/RestSharp/issues/742)

<a name="installation"></a>
## Installation
Run the following command to generate the DLL
- [Mac/Linux] `/bin/sh build.sh`
- [Windows] `build.bat`

Then include the DLL (under the `bin` folder) in the C# project, and use the namespaces:
```csharp
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;
```
<a name="packaging"></a>
## Packaging

A `.nuspec` is included with the project. You can follow the Nuget quickstart to [create](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#create-the-package) and [publish](https://docs.microsoft.com/en-us/nuget/quickstart/create-and-publish-a-package#publish-the-package) packages.

This `.nuspec` uses placeholders from the `.csproj`, so build the `.csproj` directly:

```
nuget pack -Build -OutputDirectory out IO.Swagger.csproj
```

Then, publish to a [local feed](https://docs.microsoft.com/en-us/nuget/hosting-packages/local-feeds) or [other host](https://docs.microsoft.com/en-us/nuget/hosting-packages/overview) and consume the new package via Nuget as usual.

<a name="getting-started"></a>
## Getting Started

```csharp
using System;
using System.Diagnostics;
using IO.Swagger.Api;
using IO.Swagger.Client;
using IO.Swagger.Model;

namespace Example
{
    public class Example
    {
        public static void Main()
        {
            // Configure API key authorization: LambdaTokenAuthorizer
            Configuration.Default.ApiKey.Add("Unused", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.ApiKeyPrefix.Add("Unused", "Bearer");
            // Configure API key authorization: api_key
            Configuration.Default.ApiKey.Add("x-api-key", "YOUR_API_KEY");
            // Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
            // Configuration.Default.ApiKeyPrefix.Add("x-api-key", "Bearer");

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

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://client.api.korewireless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**GetPingStatus**](docs/DefaultApi.md#getpingstatus) | **GET** /v1/ping | 
*DefaultApi* | [**V1PingOptions**](docs/DefaultApi.md#v1pingoptions) | **OPTIONS** /v1/ping | 

<a name="documentation-for-models"></a>
## Documentation for Models

 - [Model.Error](docs/Error.md)

<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="LambdaTokenAuthorizer"></a>
### LambdaTokenAuthorizer

- **Type**: API key
- **API key parameter name**: Unused
- **Location**: HTTP header

<a name="api_key"></a>
### api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

