# sz-sdk-errors

If you are beginning your journey with
[Senzing](https://senzing.com/),
please start with
[Senzing Quick Start guides](https://docs.senzing.com/quickstart/).

You are in the
[Senzing Garage](https://github.com/senzing-garage)
where projects are "tinkered" on.
Although this GitHub repository may help you understand an approach to using Senzing,
it's not considered to be "production ready" and is not considered to be part of the Senzing product.
Heck, it may not even be appropriate for your application of Senzing!

## Synopsis

This repository is used to generate multi-language source code for mapping Senzing Engine return codes into the Senzing Error Hierarchy.
The generated code is used by the Senzing SDKs.
Most likely, the generated source code has no value to a customer.

## Overview

The Senzing Error Hierarchy is:

```console
SzError
├── SzBadInputError
│   ├── SzNotFoundError
│   └── SzUnknownDataSourceError
├── SzGeneralError
│   ├── SzConfigurationError
│   ├── SzSdkError
│   └── SzReplaceConflictError
├── SzRetryableError
│   ├── SzDatabaseConnectionLostError
│   ├── SzDatabaseTransientError
│   └── SzRetryTimeoutExceededError
└── SzUnrecoverableError
    ├── SzDatabaseError
    ├── SzLicenseError
    ├── SzNotInitializedError
    └── SzUnhandledError
```

- Class hierarchy implementations:
  - [Go](https://github.com/senzing-garage/sz-sdk-go/blob/main/szerror/main.go)
    ([Local](go/main.go))
  - Java
    - Locals
  - [Python](https://github.com/senzing-garage/sz-sdk-python/blob/main/src/senzing/szerror.py)
    ([Local](python/szerror.py))

## References

1. [Development](docs/development.md)
