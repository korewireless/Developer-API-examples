# Java library for the ClientsAPI-Production

ClientsAPI-Production
- API version: 1.0.0
  - Build date: 2024-06-12T05:07:47.614382692Z[GMT]

The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.

## Overview
This API client can be used to generate an API for Client Management services in the Developer Portal.

## Requirements

Building the API client library requires:
1. Java 1.7+
2. Maven/Gradle

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>io.swagger</groupId>
  <artifactId>swagger-java-client</artifactId>
  <version>1.0.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
compile "io.swagger:swagger-java-client:1.0.0"
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/swagger-java-client-1.0.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.DefaultApi;

import java.io.File;
import java.util.*;

public class DefaultApiExample {

    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();

        // Configure API key authorization: LambdaTokenAuthorizer
        ApiKeyAuth LambdaTokenAuthorizer = (ApiKeyAuth) defaultClient.getAuthentication("LambdaTokenAuthorizer");
        LambdaTokenAuthorizer.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        //LambdaTokenAuthorizer.setApiKeyPrefix("Token");

        // Configure API key authorization: api_key
        //ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
        // api_key.setApiKey("YOUR API KEY");
        // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
        // api_key.setApiKeyPrefix("Token");

        DefaultApi apiInstance = new DefaultApi();
        String xMockResponseId = "xMockResponseId_example"; // String | 
        String authorization = "authorization_example"; // String | 
        try {
            apiInstance.getPingStatus(xMockResponseId, authorization);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#getPingStatus");
            e.printStackTrace();
        }
    }
}
import io.swagger.client.*;
import io.swagger.client.auth.*;
import io.swagger.client.model.*;
import io.swagger.client.api.DefaultApi;

import java.io.File;
import java.util.*;

public class DefaultApiExample {

    public static void main(String[] args) {
        
        DefaultApi apiInstance = new DefaultApi();
        String xMockResponseId = "xMockResponseId_example"; // String | 
        String authorization = "authorization_example"; // String | 
        try {
            apiInstance.v1PingOptions(xMockResponseId, authorization);
        } catch (ApiException e) {
            System.err.println("Exception when calling DefaultApi#v1PingOptions");
            e.printStackTrace();
        }
    }
}
```

## Documentation for API Endpoints

All URIs are relative to *https://client.api.korewireless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**getPingStatus**](docs/DefaultApi.md#getPingStatus) | **GET** /v1/ping | 
*DefaultApi* | [**v1PingOptions**](docs/DefaultApi.md#v1PingOptions) | **OPTIONS** /v1/ping | 

## Documentation for Models

 - [Error](docs/Error.md)

## Documentation for Authorization

Authentication schemes defined for the API:
### LambdaTokenAuthorizer

- **Type**: API key
- **API key parameter name**: Unused
- **Location**: HTTP header

### api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author


