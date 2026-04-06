# sz-sdk-errors

If you are beginning your journey with [Senzing],
please start with [Senzing Quick Start guides].

You are in the [Senzing Garage] where projects are "tinkered" on.
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
│   ├── SzReplaceConflictError
│   └── SzSdkError
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
  - [Go]
    ([Local Go])
  - Java
    - Locals
  - [Python]
    ([Local Python])

## References

1. [Development](docs/development.md)

[Go]: https://github.com/senzing-garage/sz-sdk-go/blob/main/szerror/main.go
[Local Go]: go/main.go
[Local Python]: python/szerror.py
[Python]: https://github.com/senzing-garage/sz-sdk-python/blob/main/src/senzing/szerror.py
[Senzing Garage]: https://github.com/senzing-garage
[Senzing Quick Start guides]: https://docs.senzing.com/quickstart/
[Senzing]: https://senzing.com/
