# KORE SDK

## Getting started

KORE Developer Portal is where you have access to all of our platform APIs in a single self-service location, providing highly secure, managed access to your services in the KORE Portal. The KORE Developer Portal is designed to make scaling your IoT applications simple and effective.

### 1. Clone the repo

````
git clone https://gitlab.com/korewireless/public/kore_sdks.git
````
### 2. SDK Collections
Client Libraries are available for the following programming language:
#### C#
- [View the SDK Documentation](csharp/README.md)
- Download the [SDK Source Code](https://gitlab.com/korewireless/public/kore_sdks/-/tree/api-clients/csharp)
#### Go
- [View the SDK Documentation](go/README.md)
- Download the [SDK Source Code](https://gitlab.com/korewireless/public/kore_sdks/-/tree/api-clients/go)
#### Java
- [View the SDK Documentation](java/README.md)
- Download the [SDK Source Code](https://gitlab.com/korewireless/public/kore_sdks/-/tree/api-clients/java)
#### Javascript
- [View the SDK Documentation](javascript/README.md)
- Download the [SDK Source Code](https://gitlab.com/korewireless/public/kore_sdks/-/tree/api-clients/javascript)
#### PHP
- [View the SDK Documentation](php/README.md)
- Download the [SDK Source Code](https://gitlab.com/korewireless/public/kore_sdks/-/tree/api-clients/php)
#### Python
- [View the SDK Documentation](python/README.md)
- Download the [SDK Source Code](https://gitlab.com/korewireless/public/kore_sdks/-/tree/api-clients/python)


***

### Authorization

By using an external identity provider (IdP), there is the option to manage user identities outside of AWS and give external user identities permissions to use AWS resources. Currently we have added a *Lambda authorizer*, an API gateway feature which uses a Lambda function to control access to our APIs. You can also update the function and connect it to your own custom auth service if you need.


## License
This project is licensed under the Apache License 2.0 - see the [![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0) file for details.
