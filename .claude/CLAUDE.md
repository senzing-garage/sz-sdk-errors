# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

sz-sdk-errors is a code generation tool that maintains Senzing error code mappings across multiple SDK languages. It uses a single JSON file as the source of truth and generates language-specific exception/error handling code for Python, Go, Java, and C#.

This is a Senzing Garage project (internal tooling, not customer-facing).

## Build Commands

```bash
make build           # Generate code for all languages
make build-python    # Generate Python exception classes
make build-go        # Generate Go error types (auto-formatted with gofmt)
make build-java      # Generate Java exception mapper
make build-csharp    # Generate C# exception mapper
make lint            # Run pylint on Python files
make help            # List all available targets
```

## Architecture

**Single source of truth:** `szerrors.json` contains all error definitions (~450 errors) with:

- `code`: Numeric error code (e.g., 2)
- `class`: Exception class name (e.g., "SzNotFoundError")
- `name`: Error identifier (e.g., "SENZ1001")
- `comment`: Error description

**Code generators** in `bin/`:

- `generate_python.py` -> `python/szerror.py`
- `generate_go.py` -> `go/szerrortypes.go`
- `generate_java.py` -> `java/SzExceptionMapper.java`
- `generate_csharp.py` -> `csharp/SzExceptionMapper.cs`

All generated files include "DO NOT EDIT" headers with generation timestamps.

## Error Hierarchy

```text
SzError (base)
|-- SzBadInputError
|   |-- SzNotFoundError
|   |-- SzUnknownDataSourceError
|-- SzGeneralError
|   |-- SzConfigurationError
|   |-- SzReplaceConflictError
|   |-- SzSdkError
|-- SzRetryableError
|   |-- SzDatabaseConnectionLostError
|   |-- SzDatabaseTransientError
|   |-- SzRetryTimeoutExceededError
|-- SzUnrecoverableError
    |-- SzDatabaseError
    |-- SzLicenseError
    |-- SzNotInitializedError
    |-- SzUnhandledError
```

## Adding New Errors

1. Add the error definition to `szerrors.json`
2. Run `make build` to regenerate all language outputs
3. Generated code will be updated in `python/`, `go/`, `java/`, and `csharp/` directories

## Linting

- Python: pylint with extended disables for generated-code patterns (see `.pylintrc`)
- Go: gofmt applied automatically during `make build-go`
- Spell checking: cspell with Senzing-specific dictionary in `.vscode/cspell.json`
