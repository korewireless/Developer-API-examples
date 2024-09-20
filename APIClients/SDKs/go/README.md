# Go API client

The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.

## Overview
This API client can be used to generate an API for Client Management services in the Developer Portal. Project Details:

- API version: 1.0.0
- Package version: 1.0.0

## Documentation for API Endpoints

All URIs are relative to *https://client.api.korewireless.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**GetPingStatus**](docs/DefaultApi.md#getpingstatus) | **Get** /v1/ping | 
*DefaultApi* | [**V1PingOptions**](docs/DefaultApi.md#v1pingoptions) | **Options** /v1/ping | 

## Documentation For Models

 - [ModelError](docs/ModelError.md)

## Documentation For Authorization

## LambdaTokenAuthorizer
- **Type**: API key 

Example
```golang
package main

import (
	"context"
	"fmt"
	"log"

	clientChk "example.com/go-client-generated"
	"github.com/antihax/optional"
)

func main() {
	fmt.Println("Hello, World!")
	//created configuration
	var cfg = clientChk.NewConfiguration()
	//created new client
	client := clientChk.NewAPIClient(cfg)
	//adding authorization string
	var localVarOptionals = &clientChk.DefaultApiGetPingStatusOpts{
		Authorization: optional.NewString("authorization_example"),
	}
	//call getclient api
	model, err := client.DefaultApi.GetPingStatus(context.Background(), localVarOptionals)
	//print result
	log.Printf("%+v %+v %+v", model, err)
}
```

Example
```golang
auth := context.WithValue(context.Background(), sw.ContextAPIKey, sw.APIKey{
	Key: "APIKEY",
	Prefix: "Bearer", // Omit if not necessary.
})
r, err := client.Service.Operation(auth, args)
```
## api_key
- **Type**: API key 

Example
```golang
auth := context.WithValue(context.Background(), sw.ContextAPIKey, sw.APIKey{
	Key: "APIKEY",
	Prefix: "Bearer", // Omit if not necessary.
})
r, err := client.Service.Operation(auth, args)
```

## Author


