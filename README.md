# g2errors

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

## Overview

The Senzing Error Hierarchy is:

```console
G2Error
├── G2BadInputError
│   ├── G2NotFoundError
│   └── G2UnknownDatasourceError
├── G2ConfigurationError
├── G2RetryableError
│   ├── G2DatabaseConnectionLostError
│   └── G2RetryTimeoutExceededError
└── G2UnrecoverableError
    ├── G2DatabaseError
    ├── G2LicenseError
    ├── G2NotInitializedError
    └── G2UnhandledError
```

- Class hierarchy implementations:
  - [Go](https://github.com/senzing-garage/g2-sdk-go/blob/main/g2error/main.go)
    - [Local](go/main.go)
  - Java
    - Locals
  - [Python](https://github.com/senzing-garage/g2-sdk-python-next/blob/main/src/senzing/g2exceptions.py)
    - [Local](python/g2errors.py)

## References

1. [Development](docs/development.md)
1. [Errors](docs/errors.md)
1. [Examples](docs/examples.md)
